# 模块 4：期刊适配（Journal Adapt）

> 增强来源：nature-style-writer（Nature 风格库）+ journal-styles/nature-cns.md（期刊风格规则库）

**触发关键词**：适配、风格、目标期刊、AAAI、ICML、NeurIPS、CVPR、IEEE、ACM、Nature、Science、Cell、PNAS、换投、reformat、template

## 工作流（两阶段）

### Phase 1 — 风格分析

1. 用户提供 3-5 篇目标期刊/会议已发表论文（或明确期刊名）
2. 提取各论文的 Style Card（10 维度）：
   - 摘要结构、引言架构、贡献表达、文献综述方式
   - 方法论描述、结果呈现、讨论风格
   - 语言特点、缺失模式、特色亮点
3. 聚合生成目标期刊的 Journal Style Card
4. 🆕 若目标为 Nature/CNS 期刊，自动加载 [journal-styles/nature-cns.md](journal-styles/nature-cns.md)

### Phase 2 — 逐节修改

1. 按 Abstract → Introduction → Related Work → Method → Experiments → Conclusion 顺序
2. 每节输入用户手稿 → 对比 Journal Style Card → 输出修订建议
3. 提供「风格差异报告」：列出与目标期刊不一致之处

---

## 🆕 内置期刊风格规则库

| 期刊/会议 | 风格文件 | 特性 |
|----------|---------|------|
| Nature 系列 | [journal-styles/nature-cns.md](journal-styles/nature-cns.md) | 7-Pass 编辑法、出版级图表、审稿视角 |
| AAAI | SKILL.md 内置 | 双栏、匿名化、页数限制 |
| ICML/NeurIPS | 待扩充 | — |
| CVPR | 待扩充 | — |
| IEEE/ACM | 待扩充 | — |

---

## 🆕 期刊风格快速对比卡

| 维度 | CS 会议（AAAI/ICML） | Nature/Science | IEEE/ACM |
|------|---------------------|---------------|----------|
| 篇幅 | 8-10 页 | 3-5 页（正文） | 8-12 页 |
| 读者 | 领域专家 | 跨学科科学家 | 领域专家 |
| 摘要 | 150-200 词，结构化 | ~150 词，叙事性 | 150-250 词 |
| 图表 | 4-6 个 | 3-4 个（高信息密度） | 4-8 个 |
| 被动语态 | 可接受 | 不推荐 | 可接受 |
| Claim 强度 | "demonstrate" | "suggest/indicate"（保守） | "demonstrate/show" |
| 补充材料 | 单独文件 | 独立 SI 文档 | 可选 |

---

## 换投场景（吸收 paper-master-opt）

当用户请求"换投"时（如从 AAAI 换到 ICML），调整路由顺序：

```
标准顺序：结构策略 → 段落润色 → LaTeX精修 → 去AI痕迹 → 审稿预检 → 期刊适配 → Cover Letter
换投顺序：期刊适配（先分析新目标）→ 段落润色（适配新风格）→ LaTeX精修（调整模板）→ 审稿预检
```

---

## 内置领域静态规则

位于 [domain-rules/](domain-rules/)：
- [ml-cv-nlp.md](domain-rules/ml-cv-nlp.md)：ML/CV/NLP 领域术语表、公式排版惯例、评测指标写法
- [cs-engineering.md](domain-rules/cs-engineering.md)：CS 工程类论文风格
- 🆕 [journal-styles/nature-cns.md](journal-styles/nature-cns.md)：Nature/CNS 期刊完整风格指南

## 与相关模块协作

- → 模块1（结构策略）：期刊风格影响结构规划
- → 模块2（段落润色）：按期刊风格执行润色
- → 模块3（LaTeX精修）：期刊模板格式检查
- → 模块9（引用验证）：期刊引用格式验证