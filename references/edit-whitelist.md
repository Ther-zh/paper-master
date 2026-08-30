# 编辑白名单协议（Edit Whitelist）

> 修改边界硬约束。用于审稿修订、换投、camera-ready、生成模式修订等需要「冻结结构」的场景，
> 防止在修改过程中偷偷新增引用、定理、实验数字。

## 何时使用

- 审稿人要求修订：只能改文字，不能加新实验/新引用
- 换投 / resubmit：论文结构冻结，只做 text-only 微调
- 生成模式修订：防止 LLM 在改写时顺手编造新内容

## 协议文件格式（YAML）

```yaml
allowed_paths:            # 可改路径（glob）；空 = 不限制路径
  - sec/*.tex
  - main.tex
forbidden_paths:          # 禁改路径（glob）；空 = 无路径限制
  - "**/*.bib"
  - "**/*.sty"
  - "**/*.bst"
forbidden_operations:     # 禁增操作（检测新增行）
  - new_cite              # 新增 \cite/\citep/\citet/\citeauthor 等
  - new_bibitem           # 新增 \bibitem
  - new_theorem_env       # 新增 \begin{theorem|lemma|proposition|corollary}
  - numerical_claim       # 新增数字/百分比/指标 token
forbidden_deletions:      # 禁删操作
  - delete_existing_cite  # 删除正文已有 \cite
  - delete_theorem_env    # 删除已有 theorem 块
requires_user_approval_for:
  - rewrite_abstract      # 整体改写摘要需人工确认
  - delete_section
max_edits_per_round: 30
rationale: "Resubmit mode: text-only microedits"
```

## 解析规则

| allowed_paths | forbidden_paths | 效果 |
|---------------|-----------------|------|
| 空 | 空 | 无操作（no-op） |
| 空 | 非空 | 除 forbidden 外皆可改 |
| 非空 | 空 | 仅 allowed 可改 |
| 非空 | 非空 | 需匹配 allowed 且不匹配 forbidden（forbidden 优先）|

glob 用 Python `fnmatch` 语义；`**` 匹配任意深度；路径相对 paper 目录。

## 操作检测正则（针对新增行）

| 操作 | 检测 |
|------|------|
| `new_cite` | `\\cite[a-zA-Z]*\{[^}]+\}` |
| `new_bibitem` | `\\bibitem\{[^}]+\}` |
| `new_theorem_env` | `\\begin\{(theorem|lemma|proposition|corollary)\*?\}` |
| `numerical_claim` | 新增 token 匹配 `\b\d+(\.\d+)?%?\b` 且不在被替换行中出现 |

## 行为

- 拒绝的编辑记录到 `REVISION_LOG.md`（文件、原因、触发的 pattern），不静默丢弃
- 单个拒绝不中止整轮；每轮结束汇总被拒数量
- 关键路径（重写摘要/删节）需要人工确认才执行

## 使用示例

```bash
# 生成模式修订，冻结 bib 与结构
python scripts/apply_whitelist.py --whitelist edit_whitelist.yaml --log REVISION_LOG.md
```
