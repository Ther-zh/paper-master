---
name: paper-master
description: >-
  一站式学术论文写作 Skill，集万家之所长，覆盖从初稿到投递的全流程：
  结构策略、段落润色（Nature 7-Pass编辑法）、LaTeX 精修（出版级图表）、
  期刊适配（Nature/CNS风格库）、审稿预检（对抗性自审+声明-证据对齐）、
  去 AI 痕迹、Cover Letter、文献调研、引用验证、学位论文、论文翻译。
  当用户提到论文写作、论文润色、LaTeX 论文、会议/期刊投稿、
  AAAI/ICML/NeurIPS/CVPR/IEEE/ACM/Nature/Science/Cell/PNAS、
  语法检查、学术写作、英文润色、去 AI 痕迹、AI 检测、humanize、
  审稿人视角、投稿前检查、cover letter、期刊风格适配、
  文献综述、引用检查、学位论文、开题报告、盲审、论文翻译时激活本 Skill。
---

# paper-master v2

一站式学术论文写作 Skill，集万家之所长，覆盖从初稿到投递的全流程。智能路由设计——只需描述你要做什么，自动匹配对应模块。

> **v2 更新**：模块从 7 个扩展到 11 个，吸收 Nature Skill 生态、scicomp-research-skills、citation-verifier、dissertation-workflow-core、arxiv-translator 等 40+ 候选中的优秀方法论。

## Quick Start

1. 描述你的需求（如「帮我润色这段 Abstract」「投稿前帮我挑毛病」「帮我做文献调研」「检查引用是否真实」）
2. paper-master 自动路由到对应模块（1~11）
3. 按模块指引逐步完成，输出结构化建议

## 触发条件

论文写作、论文润色、论文格式、论文结构、LaTeX 论文、会议论文、期刊论文、AAAI/ICML/NeurIPS/CVPR/IEEE/ACM、Nature、Science、Cell、PNAS、语法检查、学术写作、英文润色、去AI痕迹、AI检测、humanize、审稿人视角、投稿前检查、cover letter、期刊风格适配、目标期刊、换投、文献调研、文献综述、systematic review、引用检查、引用验证、citation check、DOI验证、学位论文、硕士论文、博士论文、thesis、dissertation、开题报告、盲审、答辩、论文翻译、中译英、英译中

## 11 大模块与路由规则

| 模块 | 触发关键词 | 优先级 | 来源 |
|------|-----------|--------|------|
| [模块1：结构策略](references/module-1-structure.md) | 结构/逻辑/IMRAD/规划 | P2 | 原有 |
| [模块2：段落润色](references/module-2-polish.md) | 润色/改写/paraphrase/academic/polish/proofread | P1 | 🆕 增强：Nature 7-Pass编辑法 |
| [模块3：LaTeX精修](references/module-3-latex.md) | LaTeX/编译/格式/图表/figure/table | P1 | 🆕 增强：出版级图表规范 |
| [模块4：期刊适配](references/module-4-journal.md) | 适配/风格/目标期刊/Nature/Science/换投 | P2 | 🆕 增强：Nature/CNS风格库 |
| [模块5：审稿预检](references/module-5-audit.md) | 审稿/挑毛病/投稿前/audit/review | P3 | 🆕 增强：对抗性自审 |
| [模块6：去AI痕迹](references/module-6-deai.md) | 去AI/AI痕迹/humanize | P3 | 原有 |
| [模块7：Cover Letter](references/module-7-cover-letter.md) | cover letter/投稿信 | P3 | 原有 |
| [模块8：文献调研](references/module-8-lit-review.md) | 🆕 文献调研/综述/survey/literature review/SLR/PRISMA | P2 | 🆕 新增：scicomp+SLR方法论 |
| [模块9：引用验证](references/module-9-citation-check.md) | 🆕 引用检查/DOI验证/BibTeX/citation check | P2 | 🆕 新增：citation-verifier |
| [模块10：学位论文](references/module-10-thesis.md) | 🆕 学位论文/硕士/博士/thesis/dissertation/开题/盲审/答辩 | P2 | 🆕 新增：dissertation-workflow |
| [模块11：论文翻译](references/module-11-translation.md) | 🆕 翻译/中译英/英译中/translate | P3 | 🆕 新增：arxiv-translator |

**默认组合路由**：结构策略 → 段落润色 → LaTeX精修 → 去AI痕迹 → 审稿预检 → 期刊适配 → Cover Letter

**🆕 换投路由**（吸收 paper-master-opt）：期刊适配（先分析新目标）→ 段落润色（适配新风格）→ LaTeX精修（调整模板）→ 审稿预检

**🆕 学位论文路由**：结构策略 → 文献调研 → 逐章写作（→段落润色→LaTeX精修→引用验证循环）→ 盲审检查

## 🆕 歧义处理规则（吸收 paper-master-opt）

当用户请求模糊时（如「帮我看看论文」「帮我改改论文」），不要直接应用模块。先询问：
- 「你需要我关注哪个方面？（结构/润色/格式/审稿预检/引用检查）」
- 「目标期刊/会议是？（Nature/AAAI/ICML/...）」
- 「当前处于哪个阶段？（初稿/修改/投稿前/盲审准备）」

根据回答再路由。若用户未明确说明，默认路由到模块5（审稿预检），并明确告知假设。

## 🆕 执行检查点机制（吸收 paper-master-opt）

每个模块执行完毕后，输出 1 行 summary：
```
[✓ module-X] 完成 <模块名>：共发现 X 个问题，已提供 X 条建议
```

## 润色 Prompt 模板库

详见 [polish-prompts.md](references/polish-prompts.md)，包含 6 大类 prompt 模板（语法修正、学术化改写、句式优化、段落润色、摘要润色、讨论润色）及 AI 指纹词检测清单。

## AAAI 场景默认配置

当检测到用户论文为 AAAI 投稿（如存在 `aaai2027.sty` 或用户提及）时，自动加载：
- 双栏格式检查（`\documentclass[letterpaper]{article}` 风格）
- 页数限制提醒（AAAI 2027 通常 7页正文 + 额外页）
- 匿名化检查（`\author{}` 应为 `Anonymous Submission`）
- 引用格式检查（`aaai2027.bst`）

## 🆕 Nature/CNS 场景默认配置

当检测到用户目标期刊为 Nature/Science/Cell/PNAS 时，自动加载：
- [journal-styles/nature-cns.md](references/journal-styles/nature-cns.md)：完整 Nature 风格指南
- 7-Pass 编辑法（模块2）
- 出版级图表规范（模块3）
- Nature 审稿视角（模块5）

## Agent Rules (Non-Negotiable)

1. **不代写**：模块提供建议和改进方案，不凭空生成未经用户验证的内容
2. **不编造**：永不捏造引用、数据、实验结果
3. **保留主导权**：每个修改建议标注为 `[建议]` 类，用户确认后方可应用
4. **敏感内容保护**：`\cite{}`、`\ref{}`、数学环境、图表数据永不修改

## 参考文档索引

| 文档 | 内容 |
|------|------|
| [module-1-structure.md](references/module-1-structure.md) | 结构策略工作流 |
| [module-2-polish.md](references/module-2-polish.md) | 🆕 段落润色工作流（7-Pass编辑法） |
| [module-3-latex.md](references/module-3-latex.md) | 🆕 LaTeX 精修工作流（出版级图表） |
| [module-4-journal.md](references/module-4-journal.md) | 🆕 期刊适配工作流（Nature/CNS风格库） |
| [module-5-audit.md](references/module-5-audit.md) | 🆕 审稿预检工作流（对抗性自审） |
| [module-6-deai.md](references/module-6-deai.md) | 去 AI 痕迹工作流 |
| [module-7-cover-letter.md](references/module-7-cover-letter.md) | Cover Letter 工作流 |
| 🆕 [module-8-lit-review.md](references/module-8-lit-review.md) | 文献调研与综述 |
| 🆕 [module-9-citation-check.md](references/module-9-citation-check.md) | 引用验证与格式化 |
| 🆕 [module-10-thesis.md](references/module-10-thesis.md) | 学位论文写作 |
| 🆕 [module-11-translation.md](references/module-11-translation.md) | 论文翻译 |
| [polish-prompts.md](references/polish-prompts.md) | 段落润色 Prompt 模板库 + AI 指纹词检测清单 |
| [domain-rules/ml-cv-nlp.md](references/domain-rules/ml-cv-nlp.md) | ML/CV/NLP 领域规则 |
| [domain-rules/cs-engineering.md](references/domain-rules/cs-engineering.md) | CS 工程类论文规则 |
| 🆕 [journal-styles/nature-cns.md](references/journal-styles/nature-cns.md) | Nature/CNS 期刊完整风格指南 |