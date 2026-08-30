#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""paper-master 静态 LaTeX 健康检查（无需编译）

在编译之前/之后对 .tex 源做静态体检，捕捉会让审稿人/编译器拒绝的常见问题。

用法:
  python scripts/check_tex.py paper/ [--venue iclr|neurips|icml|aaai|cvpr|ieee]
  python scripts/check_tex.py --files main.tex sections/*.tex

检查项:
  1. 未闭合环境  (\\begin 与 \\end 配对)
  2. 未定义引用   (\\ref 无对应 \\label；\\cite 无对应 bib 条目——若 bib 存在)
  3. 重复 label
  4. 理论论文一致性：正文定理/命题/引理/推论声明 与 附录证明块 的编号/重述粗查
  5. 写作残留标记: TODO / FIXME / XXX / [VERIFY] / DATA_NEEDED / lorem / placeholder
  6. 陈旧 section 文件（未被 main.tex \\input 的文件）
  7. 匿名泄漏信号（邮箱 / 真实作者名占位，仅启发式提示）

只读，不改文件。退出码: 0=无严重问题, 1=发现问题（供 CI/提交门使用）。
"""

import argparse
import re
import sys
from pathlib import Path

ENV_NAMES = [
    "figure", "figure*", "table", "table*", "equation", "equation*",
    "align", "align*", "gather", "gather*", "itemize", "enumerate",
    "theorem", "lemma", "proposition", "corollary", "proof", "definition",
    "example", "remark", "assumption", "algorithm", "algorithmic",
    "tikzpicture", "lstlisting", "verbatim", "minipage", "center",
    "abstract", "appendix", "IEEEkeywords", "IEEEbiography",
]

ISSUES = []


def add(sev, path, line, msg):
    ISSUES.append((sev, path, line, msg))


def check_envs(text, path):
    # 栈式匹配
    stack = []
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\\begin\{([^}]+)\}", line):
            stack.append((m.group(1), i))
        for m in re.finditer(r"\\end\{([^}]+)\}", line):
            if stack and stack[-1][0] == m.group(1):
                stack.pop()
            else:
                add("WARN", path, i, f"\\end{{{m.group(1)}}} 无匹配的 \\begin（或环境嵌套错误）")
    # 栈内残余 = 未闭合
    for env, i in stack:
        add("ERROR", path, i, f"\\begin{{{env}}} 未闭合")


def check_refs(text, path, bib_keys):
    labels = set(re.findall(r"\\label\{([^}]+)\}", text))
    refs = set(re.findall(r"\\ref\{([^}]+)\}", text)) | set(
        re.findall(r"\\eqref\{([^}]+)\}", text)
    ) | set(re.findall(r"\\autoref\{([^}]+)\}", text))
    for r in sorted(refs - labels):
        add("ERROR", path, 0, f"\\ref{{{r}}} 未定义（无对应 \\label）")

    if bib_keys is not None:
        cites = set()
        for m in re.finditer(r"\\cite[a-zA-Z]*\{([^}]*)\}", text):
            cites.update(k.strip() for k in m.group(1).split(",") if k.strip())
        for c in sorted(cites - bib_keys):
            add("ERROR", path, 0, f"\\cite{{{c}}} 未在 .bib 中找到条目")


def check_dup_labels(text, path):
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    seen = {}
    for lab in labels:
        seen[lab] = seen.get(lab, 0) + 1
    for lab, n in seen.items():
        if n > 1:
            add("ERROR", path, 0, f"重复 label: {lab} ({n} 次)")


def check_theorem_consistency(text, path):
    """粗查：正文声明的定理编号是否都有对应证明/附录陈述。"""
    thm_states = re.findall(
        r"\\begin\{(theorem|lemma|proposition|corollary)\*?\}(.*?)\\end\{\1\*?\}",
        text,
        re.S,
    )
    proof_count = len(re.findall(r"\\begin\{proof\}", text))
    if thm_states and proof_count < len(thm_states):
        add(
            "WARN", path, 0,
            f"理论一致性：正文声明 {len(thm_states)} 个定理/命题/引理/推论，"
            f"但仅 {proof_count} 个 proof 环境——理论论文请核对正文与附录证明一一对应",
        )
    # 术语漂移启发式（stationary vs terminal 类）——仅提示，不阻断
    for pair in [("stationary", "terminal"), ("global minima", "local minima")]:
        a = text.lower().count(pair[0])
        b = text.lower().count(pair[1])
        if a and b:
            add(
                "INFO", path, 0,
                f"术语一致性提示: '{pair[0]}' ({a} 次) 与 '{pair[1]}' ({b} 次) 同现，"
                f"若指同一概念请统一",
            )


def check_markers(text, path):
    patterns = {
        "TODO/FIXME/XXX": r"\b(TODO|FIXME|XXX|TBD)\b",
        "[VERIFY]": r"\[VERIFY\]",
        "DATA_NEEDED": r"DATA_NEEDED",
        "placeholder": r"\b(lorem ipsum|placeholder text|draft text|sample text)\b",
    }
    for name, pat in patterns.items():
        if re.search(pat, text, re.I):
            add("WARN", path, 0, f"发现写作残留标记: {name}")


def check_anonymity(text, path):
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
    for e in emails[:3]:
        add("WARN", path, 0, f"匿名模式疑似泄漏邮箱: {e}")
    if re.search(r"\\author\{[^}]*[A-Za-z]{2,}\s+[A-Za-z]{2,}\}", text):
        add("INFO", path, 0, "\\author 含疑似真实姓名，匿名投稿请改为 Anonymous Submission")


def parse_bib_keys(bib_path):
    if not bib_path:
        return None
    try:
        text = Path(bib_path).read_text(encoding="utf-8-sig", errors="ignore")
    except Exception:
        return None
    return set(re.findall(r"@\w+\{([^,]+),", text))


def main():
    ap = argparse.ArgumentParser(description="paper-master 静态 LaTeX 健康检查")
    ap.add_argument("target", nargs="?", help="论文目录或 .tex 文件")
    ap.add_argument("--files", nargs="+", help="显式列出 .tex 文件")
    ap.add_argument("--bib", help=".bib 文件路径（用于 cite 检查）")
    ap.add_argument("--venue", help="目标会议/期刊（预留，后续接入 venue 页数检查）")
    args = ap.parse_args()

    tex_files = []
    if args.files:
        tex_files = [Path(f) for f in args.files]
    elif args.target:
        t = Path(args.target)
        if t.is_dir():
            tex_files = sorted(list(t.rglob("*.tex")))
        elif t.is_file():
            tex_files = [t]
    if not tex_files:
        print("error: 未找到 .tex 文件", file=sys.stderr)
        sys.exit(2)

    bib_keys = parse_bib_keys(args.bib) if args.bib else None
    # 若没显式给 bib，在目标目录自动找 references.bib
    if bib_keys is None and args.target:
        t = Path(args.target)
        cand = t if t.is_dir() else t.parent
        for name in ("references.bib", "refs.bib", "paper.bib"):
            p = cand / name
            if p.exists():
                bib_keys = parse_bib_keys(p)
                break

    main_tex_names = {"main.tex", "paper.tex"}
    has_main = any(f.name.lower() in main_tex_names for f in tex_files)

    for f in tex_files:
        text = f.read_text(encoding="utf-8-sig", errors="ignore")
        rel = str(f)
        check_envs(text, rel)
        check_refs(text, rel, bib_keys)
        check_dup_labels(text, rel)
        check_theorem_consistency(text, rel)
        check_markers(text, rel)
        check_anonymity(text, rel)

    # 陈旧 section 文件检查（目录模式且有 main）
    if has_main and args.target and Path(args.target).is_dir():
        main_f = next(f for f in tex_files if f.name.lower() in main_tex_names)
        main_text = main_f.read_text(encoding="utf-8-sig", errors="ignore")
        for f in tex_files:
            if f.name.lower() in main_tex_names:
                continue
            if f.name not in main_text and f"input{{{f.stem}" not in main_text and f"include{{{f.stem}" not in main_text:
                add("WARN", str(f), 0, f"陈旧文件：未被 main.tex 引用（\\input/\\include）")

    sev_order = {"ERROR": 3, "WARN": 2, "INFO": 1}
    if ISSUES:
        for sev, path, line, msg in sorted(
            ISSUES, key=lambda x: (-sev_order[x[0]], x[1], x[2])
        ):
            loc = f"  at {path}:{line}" if line else f"  at {path}"
            print(f"[{sev}] {msg}{loc}")
        n_err = sum(1 for s, *_ in ISSUES if s == "ERROR")
        n_warn = sum(1 for s, *_ in ISSUES if s == "WARN")
        print(f"\n共 {len(ISSUES)} 项: {n_err} ERROR, {n_warn} WARN, "
              f"{len(ISSUES)-n_err-n_warn} INFO")
        sys.exit(1 if n_err else 0)
    else:
        print("检查通过：无问题发现")
        sys.exit(0)


if __name__ == "__main__":
    main()
