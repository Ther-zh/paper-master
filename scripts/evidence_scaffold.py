#!/usr/bin/env python3
"""evidence_scaffold.py — 生成 W5.0 审稿证据阶段四份产物骨架。

用法：
    python scripts/evidence_scaffold.py --out review_evidence \
        --title "Paper Title" --cutoff 2025-01-01 --venue NeurIPS

产物：
    EVIDENCE_FACTS.md
    DOMAIN_NARRATIVE.md
    BASELINE_GAP.md
    CLAIM_INTERROGATION.md
    evidence_manifest.json

默认拒绝覆盖已有产物；--force 才覆盖。
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def _facts(title: str, cutoff: str, venue: str) -> str:
    return f"""# EVIDENCE_FACTS

- title: {title}
- cutoff_date: {cutoff}
- venue: {venue}
- review_mode: deep
- status: TODO

## 1. Claims

| # | claim（原文/改写） | 类型（novelty/performance/theory/application） | 位置 |
|---|---|---|---|
| C1 | TODO | TODO | TODO |

## 2. Method

- 核心机制（逐条，不超过 7 条）：
  1. TODO
- 关键假设：
- 训练/推理流程：

## 3. Evidence

| claim | 证据（表/图/实验） | 数据集 | 指标 | 结果 | 是否支持 claim |
|---|---|---|---|---|---|
| C1 | TODO | TODO | TODO | TODO | yes/partial/no |

## 4. Datasets & Metrics

- 使用数据集：
- 评估指标：
- 统计口径（mean/best/seed 数）：

## 5. 未回答的问题

- TODO
"""


def _narrative(title: str, cutoff: str) -> str:
    return f"""# DOMAIN_NARRATIVE

- title: {title}
- cutoff_date: {cutoff}
- status: TODO
- 要求：300–400 词，只用 ≤ cutoff_date 的工作；每个转折点必须指到具体论文。

## Prompt

```text
You are a Senior Science Historian. Build a 300–400 word "Domain Narrative"
for the sub-field of the paper, using only work published ON OR BEFORE
{cutoff}.

Paper title/abstract: {title}

Task:
1. Arc of progress: dominant paradigm 5 years before cutoff; which papers
   changed it; where the field was at cutoff.
2. Open problems: explicitly unsolved problems in the most recent papers.
3. Significance criteria: what counted as a significant contribution at
   that moment.

Output: ## Domain History / ## Open Problems / ## Significance Criteria
```

## Domain History

TODO

## Open Problems

TODO

## Significance Criteria

TODO
"""


def _baseline_gap(title: str, cutoff: str) -> str:
    return f"""# BASELINE_GAP

- title: {title}
- cutoff_date: {cutoff}
- status: TODO
- 规则：每条必须有 reference + URL/DOI/arXiv ID；搜不到写 not_found，不写“不存在”。

## Prompt

```text
You are a ferocious benchmarking expert. Find SOTA methods and datasets the
authors should have compared against but did not. Only consider work
published ON OR BEFORE {cutoff}.

Paper: {title}

Return JSON:
{{
  "missing_baselines": [
    {{"name": "...", "reference": "Author et al., Venue Year",
      "reason": "...", "compared": "true|false|unknown", "url": "..."}}
  ],
  "missing_datasets": [...],
  "search_trace": [{{"query": "...", "source": "...", "date": "..."}}]
}}
```

## Missing Baselines

| # | name | reference | reason | compared | url |
|---|---|---|---|---|---|
| 1 | TODO | TODO | TODO | true/false/unknown | TODO |

## Missing Datasets

| # | name | reference | reason | compared | url |
|---|---|---|---|---|---|
| 1 | TODO | TODO | TODO | true/false/unknown | TODO |

## Search Trace

| query | source | date |
|---|---|---|
| TODO | TODO | TODO |

## 结论

- 漏引 baseline 数：
- 漏引 dataset 数：
- 是否影响核心 claim：
"""


def _interrogation(title: str, cutoff: str) -> str:
    return f"""# CLAIM_INTERROGATION

- title: {title}
- cutoff_date: {cutoff}
- status: TODO
- 规则：每个 major claim 至少 1 个 novelty Q（搜索接地）+ 1 个 soundness Q（原文引证）。

## Prompt（问题生成）

```text
For each major claim, generate:
1. a novelty question answerable by searching prior art published
   ON OR BEFORE {cutoff};
2. a soundness question answerable from the paper itself.

Output JSON:
{{"items":[{{"claim_id":"C1","novelty_q":"...","soundness_q":"..."}}]}}
```

## C1

### Novelty Question

TODO

### Novelty Answer

- novelty_degree: high/medium/low/incremental/none
- significance: high/medium/low/none
- answer:
- sources:

| title | authors | venue | year | url | key_finding |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

### Soundness Question

TODO

### Soundness Answer

- verdict: supported/partially_supported/unsupported/contradicted/unclear
- answer:
- evidence_quotes:

| location | quote |
|---|---|
| TODO | TODO |

- missing_evidence:

## C2

（复制 C1 结构）
"""


def scaffold(out_dir: Path | str, title: str, cutoff: str, venue: str,
             force: bool = False) -> dict:
    out = Path(out_dir)
    artifacts = {
        "EVIDENCE_FACTS.md": _facts(title, cutoff, venue),
        "DOMAIN_NARRATIVE.md": _narrative(title, cutoff),
        "BASELINE_GAP.md": _baseline_gap(title, cutoff),
        "CLAIM_INTERROGATION.md": _interrogation(title, cutoff),
    }
    existing = [name for name in artifacts if (out / name).exists()]
    if existing and not force:
        raise FileExistsError(
            "refusing to overwrite existing artifacts: %s (use --force)"
            % ", ".join(existing)
        )
    out.mkdir(parents=True, exist_ok=True)
    for name, content in artifacts.items():
        (out / name).write_text(content, encoding="utf-8")
    manifest = {
        "title": title,
        "cutoff_date": cutoff,
        "venue": venue,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": list(artifacts.keys()),
        "protocol": "module-5-evidence",
    }
    (out / "evidence_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return manifest


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Scaffold W5.0 evidence artifacts")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--title", required=True, help="paper title")
    ap.add_argument("--cutoff", required=True, help="YYYY-MM-DD (first public/submission date)")
    ap.add_argument("--venue", default="unknown", help="target venue (default: unknown)")
    ap.add_argument("--force", action="store_true", help="overwrite existing artifacts")
    args = ap.parse_args(argv)

    try:
        manifest = scaffold(args.out, args.title, args.cutoff, args.venue, args.force)
    except FileExistsError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2
    print("created %s in %s" % (", ".join(manifest["artifacts"]), args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
