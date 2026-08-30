# 工作流 W5：审计（数值 claim + 引用真实性）

> 投稿前最后一关。确保论文「说的和证据一致」。

## A. 数值 Claim 审计（Paper-to-Evidence Fidelity）

目的：每个数字/比较/范围声明都能追溯回原始结果文件。

### 七类典型数据错误（逐项排查）

| # | 失败模式 | 例子 | 检测 |
|---|---------|------|------|
| 1 | **数值夸大** | 论文 85.3%，原始 84.7% | 只允许标准舍入到显示精度 |
| 2 | **择优 seed** | 报 5 个 seed 里的最优 90.2%，均值 87.1% | 检查是否注明 average/best |
| 3 | **配置不一致** | A vs B 比较但超参/数据不同 | 核对 config |
| 4 | **聚合错误** | 声称「5 seed 平均」实际只有 3 次运行 | 数原始运行次数 |
| 5 | **差值错误** | 声称「提升 15%」实际 (85.3-73.1)/73.1=16.7% | 重算相对提升 |
| 6 | **图表不符** | caption 描述与实际图/表内容不一致 | 逐 caption 核对 |
| 7 | **范围夸大** | 「consistently outperforms」只在 2 个数据集测过 | 检查措辞 vs 评估范围 |

### 审计流程

1. 列出论文所有定量声明（位置/原文/数字）
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

## C. 综合 Verdict

- **PASS**：无 ERROR，所有 claim 有证据，引用真实且语境合适
- **WARN**：有需修正项但可投稿前修复
- **FAIL**：有造假/夸大/幻觉 → 必须修复才能投

→ 下一阶段: [W6 适配润色](workflow-W6-adapt.md) → [W7 投稿](workflow-W7-submit.md)
