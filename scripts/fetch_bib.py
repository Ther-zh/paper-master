#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""paper-master BibTeX 真实获取与卫生校验工具

从 DBLP / CrossRef 获取 publisher 验证过的真实 BibTeX，杜绝 LLM 幻觉引用，
并校验 .bib 与正文引用的卫生状况（dead entries、year/venue/author mismatch）。

用法:
  python scripts/fetch_bib.py search "attention is all you need" [--author "Vaswani"] [--max 5]
  python scripts/fetch_bib.py fetch "attention is all you need" [--author "Vaswani"] [--key vaswani2017attention]
  python scripts/fetch_bib.py doi 10.48550/arXiv.1706.03762
  python scripts/fetch_bib.py clean paper/main.tex paper/references.bib

search : DBLP 标题搜索，列出前 max 条真实记录（title/year/venue/key），不自动写文件
fetch  : DBLP 搜索取第一条命中并输出真实 .bib 条目（可选 --key 指定 citation key）
doi    : 通过 CrossRef 按 DOI 获取真实 .bib 条目
clean  : 校验引用卫生（dead entries + year/venue/author mismatch），只读不改文件

无第三方依赖（仅标准库）。网络请求失败会明确报错，绝不臆造条目。
"""

import argparse
import json
import re
import ssl
import sys
import urllib.parse
import urllib.request

UA = {
    "User-Agent": "paper-master/3.0 (academic writing skill; contact: local)"
}


def _ssl_ctx():
    """优先使用 certifi 的 CA 证书（Windows Python 默认证书链常不完整）。"""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


def http_json(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx()) as r:
        return json.load(r)


def dblp_search(title, author=None, max_hits=5):
    q = title
    if author:
        q = f"{q} {author}"
    url = f"https://dblp.org/search/publ/api?q={urllib.parse.quote(q)}&format=json&h={max_hits}"
    data = http_json(url)
    hits = (
        data.get("result", {})
        .get("hits", {})
        .get("hit", [])
    )
    out = []
    for h in hits:
        info = h.get("info", {})
        out.append(
            {
                "title": info.get("title", ""),
                "year": info.get("year", ""),
                "venue": info.get("venue", "") or info.get("journal", ""),
                "key": info.get("key", ""),
                "type": info.get("type", ""),
                "authors": [
                    a.get("text", "") for a in info.get("authors", {}).get("author", [])
                ]
                if isinstance(info.get("authors", {}).get("author", []), list)
                else [info.get("authors", {}).get("author", {}).get("text", "")],
            }
        )
    return out


def dblp_bib(dblp_key, timeout=25):
    url = f"https://dblp.org/rec/{dblp_key}.bib"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx()) as r:
        return r.read().decode("utf-8", "ignore")


def crossref_bib(doi, timeout=25):
    url = f"https://doi.org/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers={**UA, "Accept": "application/x-bibtex"})
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx()) as r:
        return r.read().decode("utf-8", "ignore")


def _rename_key(bib_text, new_key):
    m = re.match(r"@\w+\{([^,]+),", bib_text)
    if m and new_key:
        return bib_text.replace(m.group(1), new_key, 1)
    return bib_text


def fetch(title=None, author=None, doi=None, key=None):
    if doi:
        return _rename_key(crossref_bib(doi), key)
    if not title:
        raise SystemExit("error: 需要 --title 或 --doi")
    hits = dblp_search(title, author, max_hits=5)
    if not hits:
        return None
    best = hits[0]
    return _rename_key(dblp_bib(best["key"]), key), best


# ---------- clean: bib 卫生校验 ----------

def parse_bib_entries(text):
    entries = {}
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", text, re.S):
        etype, eid, body = m.group(1), m.group(2).strip(), m.group(3)
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{(.*?)\}", body, re.S):
            fields[fm.group(1).lower()] = fm.group(2)
        entries[eid] = {"type": etype, **fields}
    return entries


def extract_cited_keys(tex_text):
    keys = set()
    for m in re.finditer(r"\\cite[a-zA-Z]*\{([^}]*)\}", tex_text):
        for k in m.group(1).split(","):
            k = k.strip()
            if k:
                keys.add(k)
    return keys


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def clean(tex_files, bib_file):
    def read_utf8(p):
        return open(p, encoding="utf-8-sig", errors="ignore").read()
    tex = "\n".join(read_utf8(p) for p in tex_files)
    cited = extract_cited_keys(tex)
    bib_text = read_utf8(bib_file)
    entries = parse_bib_entries(bib_text)

    dead = sorted(set(entries) - cited)
    if dead:
        print("DEAD ENTRIES (未在正文中引用，应删除):")
        for k in dead:
            print("  ", k)

    for key in sorted(cited & set(entries)):
        e = entries[key]
        title = e.get("title", "").strip("{}")
        issues = []
        hits = []
        try:
            hits = dblp_search(title, max_hits=3)
        except Exception as ex:
            print(f"  !! {key}: DBLP 网络错误 {ex}")
            continue
        hit = hits[0] if hits else None
        source = "DBLP"
        if hit is None and e.get("doi"):
            try:
                cb = crossref_bib(e["doi"])
                parsed = parse_bib_entries(cb)
                hit = list(parsed.values())[0] if parsed else None
                source = "CrossRef"
            except Exception:
                hit = None
        if hit is None:
            print(f"VERIFY {key}: DBLP/CrossRef 均未命中，无法验证 — 保留并标注 % [VERIFY]")
            continue

        year_a = str(e.get("year", "")).strip()
        year_b = str(hit.get("year", "")).strip()
        if year_a and year_b and year_a != year_b:
            issues.append(f"year {year_a} != {year_b}")

        venue_a = e.get("journal") or e.get("booktitle") or ""
        venue_b = hit.get("journal") or hit.get("booktitle") or hit.get("venue") or ""
        if norm(venue_a) and norm(venue_b) and norm(venue_a) != norm(venue_b):
            issues.append(f"venue [{venue_a}] != [{venue_b}]")

        authors_a = [norm(a) for a in re.split(r"\s+and\s+", e.get("author", "")) if a.strip()]
        _a_b = hit.get("authors")
        if isinstance(_a_b, list):
            authors_b = [norm(a) for a in _a_b if a.strip()]
        else:
            authors_b = [norm(a) for a in re.split(r"\s+and\s+", hit.get("author", "") or "") if a.strip()]
        if authors_a and authors_b and authors_a[:2] != authors_b[:2]:
            issues.append("author list 不一致")

        if issues:
            print(f"MISMATCH {key} ({source}): " + "; ".join(issues))

    print("---")
    print(f"统计: 共 {len(entries)} 个条目, 正文引用 {len(cited)} 个 key, 死条目 {len(dead)} 个")


def main():
    ap = argparse.ArgumentParser(description="paper-master 真实 BibTeX 工具")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("search", help="DBLP 标题搜索")
    p1.add_argument("title")
    p1.add_argument("--author")
    p1.add_argument("--max", type=int, default=5)

    p2 = sub.add_parser("fetch", help="获取第一条命中的真实 BibTeX")
    p2.add_argument("title")
    p2.add_argument("--author")
    p2.add_argument("--key", help="指定 citation key")

    p3 = sub.add_parser("doi", help="按 DOI 获取真实 BibTeX")
    p3.add_argument("doi")
    p3.add_argument("--key")

    p4 = sub.add_parser("clean", help="bib 卫生校验")
    p4.add_argument("tex_files", nargs="+")
    p4.add_argument("bib_file")

    args = ap.parse_args()

    if args.cmd == "search":
        hits = dblp_search(args.title, args.author, args.max)
        if not hits:
            print("无命中")
            return
        for i, h in enumerate(hits, 1):
            print(
                f"[{i}] {h['title']} ({h['year']}) — {h['venue']}\n"
                f"     authors: {', '.join(h['authors'])}\n"
                f"     dblp key: {h['key']}"
            )
    elif args.cmd == "fetch":
        result = fetch(title=args.title, author=args.author, key=args.key)
        if result is None:
            print("error: DBLP 未命中该标题，改用 --doi 或人工确认")
            sys.exit(1)
        bib, best = result
        print(f"% source: DBLP {best['key']} — {best['title']} ({best['year']})")
        print(bib.strip())
    elif args.cmd == "doi":
        print(crossref_bib(args.doi).strip())
    elif args.cmd == "clean":
        clean(args.tex_files, args.bib_file)


if __name__ == "__main__":
    main()
