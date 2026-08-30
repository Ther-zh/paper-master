# 模块 1：结构策略（Structure Strategist）

**触发意图**：「规划论文结构」「帮我梳理逻辑」「IMRAD 结构」「实验放哪一节」「写大纲」

## 工作流

1. 分析用户提供的论文内容或研究主题
2. 按 IMRAD (Introduction / Methods / Results / Discussion) 标准检查结构
3. 输出：分节建议 + 各节核心论点清单 + 逻辑流检查
4. 与 AAAI/目标会议格式要求对齐

## 质量检查点

- 每节是否有明确的「claim - evidence - analysis」三角
- Introduction 是否从宽到窄（领域 → 问题 → gap → contribution）
- Results 与 Method 是否一一对应

---

## 🆕 Claims-Evidence Matrix（声明-证据矩阵）

规划结构前，先建立声明与证据的映射表——这是「不编造」的结构化保障：

```markdown
| Claim | Evidence | Status | Section |
|-------|----------|--------|---------|
| 方法 A 提升 3.2% | results/x.json (Ours vs Baseline) | Supported | §4.1 |
| 首次解决 Y | 文献调研确认无先例 | Unsupported → 弱化 claim | §1 |
| 可泛化到新域 | 仅 1 域实验 | Partial → 缩小 scope | §4.3 |
```

状态规则：
- **Supported**：有数据/引用/用户确认的推理
- **Partial**：证据不足 → 缩小 claim 措辞
- **Unsupported**：无证据 → 删除或改为 future work

## 🆕 GAP_REPORT（证据缺口报告）

对照论文应有的结构槽位 vs 用户实际证据，标记缺口：

```markdown
| 结构槽位 | 需要什么 | 用户证据 | 状态 | Slot ID |
|---------|---------|---------|------|---------|
| §4 消融实验 | ablation 矩阵 | 无 | missing | GAP_S4_ABLATION |
| §2 Related | 引用密度 ≥ 60 | bib 35 条 | partial | GAP_S2_CITES |
| §5 失败案例 | failure-case 分析 | narrative 无 | missing | GAP_S5_FAILURE |
```

Slot ID 格式：`GAP_<SECTION>_<FEATURE>`（全大写，稳定）。

**硬规则**：
- 缺口就是缺口，**绝不推断/填充/编造证据**
- missing 槽位在写作阶段输出 `<!-- DATA_NEEDED: GAP_S4_ABLATION -->` 占位，不虚构内容
- 缺口清单直接呈现给用户，不隐藏

## 结构模板（按论文类型）

### 实证型（Empirical）
```
1. Introduction (宽→窄漏斗 + contribution)
2. Related Work (≥1 页，真实引用)
3. Method
4. Experiments (消融/对比/分析，每 claim 有证据)
5. Conclusion / Limitations
```

### 理论型（Theory）
```
1. Introduction
2. Notation & Preliminaries
3. Main Results (Theorem/Lemma/Corollary)
4. Proofs（或移附录，正文与附录重述必须一致——见模块3定理一致性）
5. Discussion
```

## 与相关模块协作

- → 模块4（期刊适配）：期刊风格影响结构
- → 生成模式：产出 PAPER_PLAN.md 供 W2 写作使用（见 workflow-W1-plan.md）
- → 模块9（引用验证）：Related Work 的引用需真实
