# 工作流 W5：审计（数值 claim + 引用真实性）

> 投稿前最后一关。确保论文「说的和证据一致」。

## W5.0 审稿证据阶段（先取证，再评审）

深度审稿 / 审稿意见回复 / 高风险论文先跑：

```bash
python scripts/evidence_scaffold.py --out review_evidence \
  --title "Paper Title" --cutoff 2025-01-01 --venue NeurIPS
```

1. 确定 `cutoff_date`（论文首次公开/投稿日期）。
2. 产出 `EVIDENCE_FACTS.md`（claims/method/evidence/datasets/metrics）。
3. 产出 `DOMAIN_NARRATIVE.md`（演进弧 + open problems + significance criteria）。
4. 产出 `BASELINE_GAP.md`（漏引 baseline/dataset，逐条带 reference + URL + compared）。
5. 产出 `CLAIM_INTERROGATION.md`（每个 major claim：novelty Q 搜索接地 + soundness Q 原文引证）。

**硬规则**：novelty 检索只用 ≤ cutoff_date 的工作；来源限顶会/顶刊 + arXiv；
每条外部证据必须有 URL/DOI/arXiv ID；“没搜到”写 `not_found`，不写“不存在”。
完整 prompt/schema/预算见 [module-5-evidence.md](module-5-evidence.md)。
模块 5 的深度评审报告若没有以上四份产物，只能标 `review_mode: quick`。

## A. 数值 Claim 审计（Paper-to-Evidence Fidelity）

目的：每个数字/比较/范围声明都能追溯回原始结果文件。

### 九类典型数据错误（逐项排查）

| # | 失败模式 | 例子 | 检测 |
|---|---------|------|------|
| 1 | **数值夸大** | 论文 85.3%，原始 84.7% | 只允许标准舍入到显示精度 |
| 2 | **择优 seed** | 报 5 个 seed 里的最优 90.2%，均值 87.1% | 检查是否注明 average/best |
| 3 | **配置不一致** | A vs B 比较但超参/数据不同 | 核对 config |
| 4 | **聚合错误** | 声称「5 seed 平均」实际只有 3 次运行 | 数原始运行次数 |
| 5 | **差值错误** | 声称「提升 15%」实际 (85.3-73.1)/73.1=16.7% | 重算相对提升 |
| 6 | **图表不符** | caption 描述与实际图/表内容不一致 | 逐 caption 核对 |
| 7 | **范围夸大** | 「consistently outperforms」只在 2 个数据集测过 | 检查措辞 vs 评估范围 |
| 8 | **图内文字失配**（v3.2） | 图上标「≤1 次」但证据/正文为「≤12 轮」；图内用词未随术语账本更新 | 抽取图内文字 ↔ 正文/caption/证据/账本 逐条核对 |
| 9 | **自由参数敏感性缺失**（v3.2） | 指标含 λ 但只报单点、无翻转点（λ≈0.025 教训） | 要求敏感性/翻转点，否则限缩到正式口径 |

### 审计流程

1. 列出论文所有定量声明（位置/原文/数字，**含图内文字**）
2. 逐个追溯：哪个结果文件？确切值？状态（exact_match / rounding_ok / mismatch）
3. 产出 `CLAIM_AUDIT.md`：

```markdown
| # | 位置 | 论文值 | 证据值 | 状态 | 修复 |
|---|------|--------|--------|------|------|
| 1 | Table 2 | 85.3% | 85.28% | rounding_ok | - |
| 2 | Abstract | 提升 15% | 12.8% | number_mismatch | 改为 12.8% |
```

### 审计独立性原则

- 若可用外部跨模型审查者，让**无上下文的新线程**只读「论文 + 原始结果文件」独立核对（避免执行者自我确认偏误）
- 无外部审查者时，至少以「假装刚接手、只看证据文件」的心态自审

## B. 引用审计（Citation Audit）

三层验证（见 module-9）：
1. **Existence**：条目真实存在（arXiv ID/DOI/venue 可解析）
2. **Metadata**：作者/年份/venue/标题与权威源一致（DBLP/arXiv/ACL）
3. **Context appropriateness**：被引论文**真的支持**它所在的 claim（危险的是「真实论文用错语境」）

逐条判定 `KEEP / FIX / REPLACE / REMOVE`：
- KEEP：条目干净且语境合适
- FIX：元数据需修正
- REPLACE：错语境引用，找真正支撑该 claim 的论文
- REMOVE：幻觉/无法支撑

> 对每条需要真实核验的引用，可借助 `scripts/fetch_bib.py` 的 DBLP/CrossRef 链辅助。

## C. 一致性审计（v3.2 新增：账本 → 审计项）

> 对象：W1 的三类账本（见 [ledgers.md](ledgers.md)）。原则：**抽查核账，不现补账本**。

| # | 审计项 | 动作 | 检出处置 |
|---|--------|------|----------|
| C1 | **机制覆盖** | 读机制注册表，逐条 core 检查正文是否按六槽展开（与复杂度信号对照，防"小体量高复杂度"被一句带过）；supporting 是否有交代 | 补写或说明豁免 |
| C2 | **图-文-码一致性** | 图内文字（标题/标签/注释）逐条对照 ①正文与 caption ②证据值 ③术语账本。有矢量/源码（SVG/TikZ/绘图脚本）→ 抽取文字清单 diff；只有位图/PDF → 人工读图填清单（图号 \| 图内文字 \| 应取值/用词 \| 来源），**禁止声称"已自动核对"** | 矢量源重导出改图，或改正文 |
| C3 | **术语漂移** | 扫描正文/图注/图内文字是否出现术语账本 replace 列原词；define_once 词是否首现定义 | 替换为论文用词 |
| C4 | **设计-实现差异** | 对照台账逐条核对锚点与状态；`unknown` 项是否仍以已实现口吻出现 | 降级措辞或补证据 |
| C5 | **自由参数敏感性** | 指标含自由参数/阈值/权重/选取规则的比较 claim，是否有敏感性分析或翻转点（见第 9 类数据错误） | 补敏感性实验或限缩措辞 |

> 独立性：C2 优先用"只读论文 + 图源 + 证据"的无上下文线程执行（见「审计独立性原则」）。

## D. 综合 Verdict

- **PASS**：无 ERROR，所有 claim 有证据，引用真实且语境合适，一致性审计 C 无遗留项；
  深度审稿还要求 W5.0 四份证据产物存在且无未解释的 `BASELINE_GAP` / `CLAIM_INTERROGATION` 项
- **WARN**：有需修正项但可投稿前修复
- **FAIL**：有造假/夸大/幻觉 → 必须修复才能投

→ 下一阶段: [W6 适配润色](workflow-W6-adapt.md) → [W7 投稿](workflow-W7-submit.md)
