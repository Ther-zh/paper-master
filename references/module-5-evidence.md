# 模块 5.0：审稿证据阶段（Evidence before Critique）

> 来源吸收：ScholarPeer（arXiv:2601.22638）的多智能体审稿框架。
> 论文在 ~1,786 篇 ICLR 2020–2025 投稿上报告：去掉 Q&A 引擎胜率 -26%，去掉 baseline scout -9%，
> 去掉 summary -10%，去掉 historian -4%，去掉 literature review -6%。
> 本文件只迁移**机制**（先取证、再评审、逐 claim 对账），不迁移其 headline 数字。

## 0. 什么时候用

| 场景 | 用不用 | 说明 |
|---|---|---|
| 投稿前深度自审 / 预答辩 / 审稿意见回复 | **必用** | 需要可核验的漏引 baseline、逐 claim 证据 |
| 给他人论文写 review / meta-review | **必用** | 把“凭记忆挑毛病”换成“有出处的审计” |
| 快速语言润色 / 格式检查 | 不用 | 直接走模块 2/3 |
| 纯文献调研 | 不用本文件 | 走 `paper-research-master`，本文件只消费其检索结果 |

**硬规则**：模块 5 的评审报告如果没有本阶段产物，只能标 `review_mode: quick`，
不得声称“已做深度审稿”。

### 快速开始

```bash
python scripts/evidence_scaffold.py \
  --out review_evidence \
  --title "Paper Title" \
  --cutoff 2025-01-01 \
  --venue NeurIPS
```

生成四份骨架 + `evidence_manifest.json`；已有产物时默认拒绝覆盖，`--force` 才覆盖。

## 1. 输入与时间边界

开始前必须确定：

```yaml
paper_text: "<PDF 提取文本或章节文件>"
paper_title: "<标题>"
cutoff_date: "<论文首次公开/投稿日期 YYYY-MM-DD>"
venue: "<目标会议/期刊；用于 review guidelines>"
domain_hint: "<可选：子领域>"
```

- **cutoff_date 是硬边界**：所有 novelty 检索只允许 ≤ cutoff_date 的工作。
  用论文发表后的工作判断“当时的新颖性”属于时代错位。
- 如果无法确定 cutoff_date：用 arXiv v1 日期；仍无法确定 → 在报告里标
  `cutoff_date: unknown`，所有 novelty 结论降级为 `provisional`。
- **来源白名单**：顶会/顶刊（NeurIPS/ICLR/ICML/CVPR/ACL/EMNLP/AAAI/IJCAI/KDD…）+ arXiv。
  博客、媒体、未知聚合站不作为 novelty 证据；需要时只作线索并标 `non-authoritative`。
- **禁止凭记忆写 URL**：所有引用必须有可解析的 arXiv ID / DOI / 会议页面；
  检索不到 → 写 `not_found`，不要编造。

## 2. 四份产物

| 产物 | 作用 | 最低要求 |
|---|---|---|
| `EVIDENCE_FACTS.md` | 论文事实表 | claims / method / evidence / datasets / metrics 五项齐全 |
| `DOMAIN_NARRATIVE.md` | 领域演进叙事 | 300–400 词：演进弧 + open problems + significance criteria |
| `BASELINE_GAP.md` | 漏引 baseline/dataset | 每条含 name / reference / reason / compared 状态 |
| `CLAIM_INTERROGATION.md` | 逐 claim 审问日志 | 每个 major claim 至少 1 个 novelty Q + 1 个 soundness Q，附证据 |

> 这四份产物是模块 5 五视角评审的**输入**，不是评审报告的附件装饰。
> 评审报告里的每条 Critical/Major 必须能指回其中一行。

## 3. Step 1：事实表（Summary Agent）

目的：把“读全文”变成可复核的结构化信号，避免 lost-in-the-middle。

```markdown
# EVIDENCE_FACTS

## 1. Claims
| # | claim（原文/改写） | 类型（novelty/performance/theory/application） | 位置 |
|---|---|---|---|
| C1 | ... | ... | Abstract / §1 / §4 |

## 2. Method
- 核心机制（逐条，不超过 7 条）：
- 关键假设：
- 训练/推理流程：

## 3. Evidence
| claim | 证据（表/图/实验） | 数据集 | 指标 | 结果 | 是否支持 claim |
|---|---|---|---|---|---|
| C1 | Table 1 | ... | ... | ... | yes/partial/no |

## 4. Datasets & Metrics
- 使用数据集：
- 评估指标：
- 统计口径（mean/best/seed 数）：

## 5. 未回答的问题
- ...
```

**质量门**：每个 claim 必须有位置；每个 performance claim 必须有数据集/指标/结果；
找不到证据的 claim 标 `unsupported`，不要替作者补。

## 4. Step 2：领域叙事（Historian Agent）

目的：给 novelty/significance 一个“当时”的坐标系，而不是 2026 年的后见之明。

### Prompt

```text
You are a Senior Science Historian. Build a 300–400 word "Domain Narrative"
for the sub-field of the paper, using only work published ON OR BEFORE
{cutoff_date}.

Input:
- Paper title/abstract: {title_abstract}
- Literature review JSON: {literature_review_json}

Task:
1. Arc of progress: what was the dominant paradigm 5 years before the cutoff?
   Which papers changed it? Where was the field at the cutoff?
2. Open problems: what did the most recent papers explicitly list as unsolved?
3. Significance criteria: at this moment, what counts as a "significant"
   contribution in this sub-field? (e.g., new capability > small metric gain;
   efficiency/interpretability may matter more than another 0.2 point.)

Output (Markdown):
## Domain History
## Open Problems
## Significance Criteria
```

**质量门**：叙事中每个“转折点”必须能指到一篇具体论文；指不到 → 删除该句。

## 5. Step 3：漏引 baseline / dataset（Baseline Scout）

目的：把“Related work 可能漏了”从感觉变成可核验清单。

### Prompt

```text
You are a ferocious benchmarking expert. Your only job is to find what the
authors are HIDING: state-of-the-art methods and datasets they should have
compared against but did not.

Paper: {paper_text}
Cutoff: only consider work published ON OR BEFORE {cutoff_date}.

Task:
1. Identify the research domain, datasets used, and baselines compared.
2. Search recent SOTA methods (last 3 years before cutoff) for this domain.
3. Identify specific methods/datasets MISSING from the authors' list.
4. For each, explain why it is a critical omission.

Output JSON:
{
  "missing_baselines": [
    {"name": "...", "reference": "Author et al., Venue Year",
     "reason": "...", "compared": false, "url": "..."}
  ],
  "missing_datasets": [
    {"name": "...", "reference": "...", "reason": "...", "compared": false, "url": "..."}
  ],
  "search_trace": [
    {"query": "...", "source": "...", "date": "..."}
  ]
}
```

**质量门**：
- 每条必须有 `reference` + `url`（arXiv/DOI/会议页）；没有 → 移到“线索”而非结论。
- `compared` 只能是 `true/false/unknown`；不确定不要写 false。
- 如果确实没有漏引：输出空列表 + search_trace，不要为了凑数编造。

## 6. Step 4：逐 claim 审问（Multi-Aspect Q&A）

目的：把“审稿意见”拆成可验证的问答题，novelty 靠外部检索，soundness 靠论文内部证据。

### 6.1 生成问题

```text
You are a critical top-tier conference reviewer. For each major claim below,
generate two questions:

1. Novelty question: a simple, direct question that a research assistant
   (who does not have the paper) can answer by searching prior art. Ask what
   is new and significant relative to work published ON OR BEFORE {cutoff_date}.
2. Soundness question: a question that can be answered from the paper itself,
   targeting internal logical consistency, experimental validity, or
   mathematical rigor.

Claims: {claims}
Paper summary: {summary}
Domain narrative: {domain_narrative}
Missing baselines/datasets: {baseline_gap}

Output JSON:
{"items":[{"claim_id":"C1","novelty_q":"...","soundness_q":"..."}]}
```

### 6.2 回答 novelty（搜索接地）

```text
You are an AI researcher with search access. Answer the novelty question
using only prior art published ON OR BEFORE {cutoff_date}.

Steps:
1. Identify the key domain and relevant top-tier venues.
2. Search arXiv + top-tier venues for the closest prior work.
3. Decide: novelty degree = high / medium / low / incremental / none.
4. Decide: significance = high / medium / low / none, with reasoning.
5. Cite 2–3 most relevant papers: title, authors, venue, year, key finding.

Output JSON:
{
  "claim_id": "C1",
  "novelty_degree": "high|medium|low|incremental|none",
  "significance": "high|medium|low|none",
  "answer": "...",
  "sources": [
    {"title": "...", "authors": "...", "venue": "...", "year": 2024,
     "url": "...", "key_finding": "..."}
  ],
  "search_trace": [{"query": "...", "source": "..."}]
}
```

### 6.3 回答 soundness（论文内部）

```text
You are a rigorous reviewer. Answer the soundness question using ONLY the
paper's own claims, method, and evidence. Quote the exact sentences/tables
you rely on. Do not use external search for this step.

Output JSON:
{
  "claim_id": "C1",
  "verdict": "supported|partially_supported|unsupported|contradicted|unclear",
  "answer": "...",
  "evidence_quotes": [
    {"location": "§4.1 / Table 1", "quote": "..."}
  ],
  "missing_evidence": ["..."]
}
```

**质量门**：
- novelty 答案必须带 sources；没有 sources 的“高新颖性”结论不可用。
- soundness 答案必须带原文引文；引文对不上 → `unclear`。
- `claimed novelty` 与 `assessed novelty` 不一致时，在报告里单列“novelty 偏差”。

## 7. Step 5：合成到模块 5

把四份产物喂给模块 5 的五视角评审，而不是让评审者从零读论文：

| 模块 5 视角 | 消费的证据 |
|---|---|
| 方法学审稿人 | `EVIDENCE_FACTS` 的 method/evidence + `CLAIM_INTERROGATION` soundness |
| 领域审稿人 | `DOMAIN_NARRATIVE` + `BASELINE_GAP` |
| 批判审稿人 | `CLAIM_INTERROGATION` 的 novelty 偏差 + unsupported claims |
| 语言审稿人 | 原文（不需要证据阶段） |
| Nature 审稿人 | `DOMAIN_NARRATIVE` 的 significance criteria + `BASELINE_GAP` |

**报告硬规则**：
1. 每条 Critical/Major 必须附 `证据位置`（artifact + 行/表/引文）。
2. 每条“缺 baseline”必须指 `BASELINE_GAP` 的具体行，不能写“相关领域可能还有”。
3. 每条“novelty 不足”必须指 `CLAIM_INTERROGATION` 的 source；没有 source → 降级为“待核实”。
4. 不允许把“我没搜到”写成“不存在”；写 `not_found` + search trace。

## 8. 检索纪律与预算

### 8.1 Cutoff / 来源 / 追踪

- 所有检索 prompt 必须带 `{cutoff_date}`，并在输出里回填 `search_trace`。
- 来源白名单：顶会/顶刊 + arXiv；其他来源只作线索。
- 每条外部证据必须有 `url`；没有 URL 的条目不能进入结论。
- 论文发表后的工作只能放在“后续工作”小节，不能用于 novelty 判定。

### 8.2 预算（来自 ScholarPeer 的饱和点）

| 模式 | expansion rounds | QA pairs | 适用 |
|---|---|---|---|
| quick | 1 | 3–4 | 快速自查，只覆盖核心 claim |
| standard | 2 | 6–8 | 常规投稿前 |
| deep | 3 | 10 | 高风险论文 / 审稿意见回复 |

> 论文报告：10 个 QA pair、3 轮 expansion 后收益饱和；继续加会稀释上下文。
> 不要默认开 deep；按风险选档。

### 8.3 独立性

- 证据阶段最好由**无上下文的新线程**执行；至少不要先把作者的摘要/辩解喂给检索者。
- 检索者只拿 `paper_text + cutoff_date + 问题`，不拿“作者认为的贡献”。
- 评审者拿证据产物 + 原文，不拿执行者的结论。

## 9. 与其他 skill 的分工

| 任务 | 用谁 |
|---|---|
| 已引文献真实性/元数据/语境 | `citation-audit`（模块 9） |
| 漏引 baseline/dataset | 本文件 Step 3（baseline scout） |
| 单篇论文精读/笔记 | `paper-research-master` P3 Deep Dive |
| 领域全景/综述 | `paper-research-master` P1–P6 |
| 数值 claim 核对 | `paper-master` W5-A（九类数据错误） |
| 对抗性 reject 论证 | `kill-argument` |
| novelty 快速判定 | `novelty-check` + 本文件 cutoff 纪律 |

## 10. 红线

1. **不编造引用/URL/检索结果**；搜不到就写 `not_found`。
2. **不用发表后的工作判断当时 novelty**；cutoff_date 是硬边界。
3. **不把“没搜到”写成“不存在”**；区分 `not_found` 与 `no_prior_art`。
4. **不替作者补实验/补数字**；缺证据写 `missing_evidence`。
5. **不把 LLM judge 的分数当终审**；证据产物是输入，人类裁决是终点。
