# 工作流 W1：规划（Claims-Evidence Matrix + GAP_REPORT）

> 生成模式的第二阶段。把研究叙事变成「有证据背书的结构化论文蓝图」。

## Step 1：构建 Claims-Evidence Matrix

从 `narrative.md` / `CLAIMS_FROM_RESULTS.md` 提取核心声明并映射证据：

```markdown
| Claim | Evidence | Status | Section |
|-------|----------|--------|---------|
| 方法 A 在基准 X 上超过 SOTA 3.2% | results/x.json, Ours vs Best-Baseline | Supported | §4.1 |
| 方法 A 具有理论保证 | 用户确认的引理（定理 1） | Supported (user-verified) | §3 |
| 方法 A 可泛化到新域 | 仅 1 个域验证 | Partial → 弱化为 "on this domain" | §4.3 |
```

状态分类：
- **Supported**：有数据/引用/用户确认的推理支撑
- **Partial**：证据不完整 → 缩小 claim 范围
- **Unsupported**：无证据 → 删除或降级为「未来工作」
- **Unadjudicated**：用户口头声称无原始数据 → 用 `[unadjudicated]` 标注

## Step 2：确定论文类型与结构

| 论文类型 | 结构特征 |
|---------|---------|
| 实证型 (empirical) | Intro → Related → Method → Experiments → Discussion |
| 理论型 (theory) | 增加 Notation / Theorem / Proof，正文定理 ↔ 附录全证明 |
| 方法型 (method) | 方法占主导，实验验证核心机制 |

## Step 3：GAP_REPORT（证据缺口报告）

对照论文结构槽位 vs 用户实际证据，逐槽分类：

```markdown
| 结构槽位 | 需要什么 | 用户证据 | 状态 | Slot ID |
|---------|---------|---------|------|---------|
| §4 消融实验 | ablation 矩阵 | 无 | missing | GAP_S4_ABLATION |
| §4.2 缩放规律 | log-N 曲线 | 无 | missing | GAP_S4_SCALING |
| §2 Related | 引用密度 ≥ 60 | bib 35 条 | partial | GAP_S2_CITES |
| §5 失败案例 | failure-case 分析 | narrative 无 | missing | GAP_S5_FAILURE |
```

Slot ID 格式：`GAP_<SECTION>_<FEATURE>`，全大写，保持稳定。

## Step 4：输出

- `PAPER_PLAN.md`：分节大纲 + 每节 claim/证据/图表计划
- `GAP_REPORT.md`：上表（作为 W2 写作的契约）

## 硬规则

- **绝不推断、填充、编造证据来「补缺口」**。missing 就是 missing
- 缺口直接暴露给用户，不隐藏、不粉饰
- GAP_REPORT 用于 W2 生成 `<!-- DATA_NEEDED -->` 占位，不用于编造内容

→ 下一阶段: [W2 写作](workflow-W2-write.md)
