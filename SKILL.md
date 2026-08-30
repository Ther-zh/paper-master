---
name: paper-master
description: >-
  一站式学术论文全生命周期写作 Skill，集万家之所长，覆盖从研究证据到投稿的全流程：
  研究叙事输入契约、Claims-Evidence 规划、受证据约束的论文生成（真实写作）、
  出版级图表、LaTeX 编译校验、引用真实性获取（DBLP/CrossRef）、数值 claim 审计、
  段落润色（Nature 7-Pass）、审稿预检、期刊适配、去 AI 痕迹、Cover Letter、
  文献调研、引用验证、学位论文、论文翻译。
  双模式：咨询模式（默认，给结构化建议）+ 生成模式（从 NARRATIVE_REPORT/证据真实写作）。
  当用户提到论文写作、写论文、论文生成、论文润色、LaTeX 论文、会议/期刊投稿、
  AAAI/ICML/NeurIPS/CVPR/IEEE/ACM/Nature/Science/Cell/PNAS、
  语法检查、学术写作、英文润色、去 AI 痕迹、AI 检测、humanize、
  审稿人视角、投稿前检查、cover letter、期刊风格适配、换投、
  文献综述、引用检查、引用验证、citation check、DOI验证、学位论文、
  开题报告、盲审、答辩、论文翻译时激活本 Skill。
---

# paper-master v3

一站式学术论文全生命周期写作 Skill。v3 从「纯咨询顾问」升级为「**真实写作引擎 + 全流程质检**」：
既能对已有论文给出专家级建议，也能从研究证据生成一篇可以编译、通过审计的论文草稿。

> **v3 更新**：
> - 🆕 **双模式**：咨询模式（默认，建议式）+ 生成模式（真实写作）
> - 🆕 **全生命周期工作流** W0→W7：输入契约 → 规划 → 生成 → 图表 → 编译 → 审计 → 适配 → 投稿
> - 🆕 **证据约束机制**：Claims-Evidence Matrix、GAP_REPORT、DATA_NEEDED 占位（绝不编造）
> - 🆕 **可执行脚本**：`scripts/fetch_bib.py`（真实 BibTeX 获取链）、`scripts/check_tex.py`（静态健康检查）
> - 🆕 **数值 claim 审计**：七类数据错误检测（数值夸大/择优seed/配置不一致/聚合错误等）
> - 🆕 **编辑白名单**：修改边界硬约束（保护 cite/ref/定理/数字）

## Quick Start

1. 描述你的需求（如「帮我润色这段 Abstract」「投稿前帮我挑毛病」「帮我做文献调研」「检查引用是否真实」「**基于这份实验结果帮我写一篇论文**」）
2. paper-master 自动判断模式并路由到对应模块（1~11）或全生命周期工作流
3. 按指引逐步完成，输出结构化结果

---

## 🎭 双模式

### 模式 A：咨询模式（Advisory，默认）

- **适用**：已有论文草稿，需要润色/审稿/排版/引用检查/换投
- **行为**：输出结构化建议与 `[建议]` 标注，用户确认后才修改
- **保持**：不代写、不编造、保留主导权、保护 cite/ref/数学/图表数据

### 模式 B：生成模式（Generation，显式开启）

- **触发**：用户说「写论文」「从结果生成论文」「write paper」「draft from results」，或传入 `NARRATIVE_REPORT.md`
- **行为**：基于研究证据**真实写作**完整论文草稿（LaTeX），可编译、可审计
- **铁律（非协商）**：
  1. **只写证据支持的内容**。每个 claim 必须映射到证据（实验数据/引用/用户确认的推理）
  2. **缺数据就写 `<!-- DATA_NEEDED: <slot> -->` 占位**，绝不自行发明数字/结果/引用
  3. **引用必须真实**：优先用 `scripts/fetch_bib.py` 从 DBLP/CrossRef 拉取；拉不到标 `% [VERIFY]`
  4. **不生成作者身份**：用匿名 author 块（`Anonymous Submission`）
  5. 生成后必须运行 `scripts/check_tex.py` 自检

---

## 🔄 全生命周期工作流（生成模式）

```
W0 输入契约 ──> W1 规划 ──> W2 生成 ──> W3 图表 ──> W4 编译校验
   (NARRATIVE    (Claims-      (逐节 LaTeX    (可选)      (check_tex.py
    _REPORT)     Evidence      写作 +         出图)        + latexmk)
                 Matrix +      DATA_NEEDED)
                 GAP_REPORT          │
                                     ▼
W7 投稿 ──> W6 适配/润色 ──> W5 审计 ──────────────┘
(Cover Letter) (期刊适配/去AI/润色)  (数值claim审计 + 引用审计)
```

| 阶段 | 名称 | 关键动作 | 产出 |
|------|------|---------|------|
| W0 | 输入契约 | 读取/询问 NARRATIVE_REPORT、实验结果、证据文件 | `narrative.md`（缺失则引导生成）|
| W1 | 规划 | Claims-Evidence Matrix + GAP_REPORT + 分节计划 | `PAPER_PLAN.md`、`GAP_REPORT.md` |
| W2 | 生成 | 逐节写作 LaTeX（受证据约束） | `paper/sections/*.tex`、`references.bib` |
| W3 | 图表 | 数据驱动出图 + 规范检查（可选） | `paper/figures/*` |
| W4 | 编译校验 | `check_tex.py` + latexmk 编译 + 页数校验 | `paper/main.pdf` |
| W5 | 审计 | 数值 claim 审计 + 引用真实性/上下文审计 | 审计报告 |
| W6 | 适配润色 | 期刊风格适配 + 7-Pass 润色 + 去AI | 修订稿 |
| W7 | 投稿 | Cover Letter、合规检查 | 投稿材料 |

**各阶段详细指引**见 `references/workflow-W0-input.md`、`references/workflow-W1-plan.md`、`references/workflow-W2-write.md`、`references/workflow-W4-compile.md`、`references/workflow-W5-audit.md`。

---

## 🧩 11 大模块与路由规则

| 模块 | 触发关键词 | 优先级 | v3 增强 |
|------|-----------|--------|---------|
| [模块1：结构策略](references/module-1-structure.md) | 结构/逻辑/IMRAD/规划/大纲 | P2 | 🆕 Claims-Evidence Matrix + GAP_REPORT + DATA_NEEDED |
| [模块2：段落润色](references/module-2-polish.md) | 润色/改写/paraphrase/polish/proofread | P1 | 🆕 Banana Rule 术语一致 + 数值/结论强度保护 |
| [模块3：LaTeX精修](references/module-3-latex.md) | LaTeX/编译/格式/图表/figure/table | P1 | 🆕 `check_tex.py` 静态体检 + 页数/溢出校验 + 定理一致性 |
| [模块4：期刊适配](references/module-4-journal.md) | 适配/风格/目标期刊/换投 | P2 | 🆕 IEEE 规范 + 系统论文蓝图（venue/ieee.md）|
| [模块5：审稿预检](references/module-5-audit.md) | 审稿/挑毛病/投稿前/audit/review | P3 | 🆕 七类数值 claim 审计 + 编辑白名单 + 跨模型独立性原则 |
| [模块6：去AI痕迹](references/module-6-deai.md) | 去AI/AI痕迹/humanize | P3 | 沿用 |
| [模块7：Cover Letter](references/module-7-cover-letter.md) | cover letter/投稿信 | P3 | 沿用 |
| [模块8：文献调研](references/module-8-lit-review.md) | 文献调研/综述/survey/SLR/PRISMA | P2 | 沿用 |
| [模块9：引用验证](references/module-9-citation-check.md) | 引用检查/DOI验证/BibTeX/citation | P2 | 🆕 `fetch_bib.py` 真实获取链 + 引用上下文适切性审计 |
| [模块10：学位论文](references/module-10-thesis.md) | 学位论文/硕博/thesis/开题/盲审 | P2 | 沿用 |
| [模块11：论文翻译](references/module-11-translation.md) | 翻译/中译英/英译中/translate | P3 | 沿用 |

**默认组合路由**：结构策略 → 段落润色 → LaTeX精修 → 去AI痕迹 → 审稿预检 → 期刊适配 → Cover Letter

**换投路由**：期刊适配（先分析新目标）→ 段落润色（适配新风格）→ LaTeX精修（调整模板）→ 审稿预检

**学位论文路由**：结构策略 → 文献调研 → 逐章写作（→段落润色→LaTeX精修→引用验证循环）→ 盲审检查

**🆕 生成路由**（检测到生成意图）：W0 输入契约 → W1 规划 → W2 生成 → W4 编译校验 → W5 审计 → W6 适配

---

## 🆕 模式判别规则

当请求模糊时（「帮我看看论文」「帮我改改论文」），先询问而不是直接套模块：
- 「你需要我关注哪个方面？（结构/润色/格式/审稿预检/引用检查）」
- 「目标期刊/会议是？（Nature/AAAI/ICML/IEEE/...）」
- 「当前处于哪个阶段？（初稿/修改/投稿前/盲审准备）」

**生成模式判别**：出现以下任一信号 → 进入生成模式：
- 用户明确要求写/生成/起草论文
- 用户提供 `NARRATIVE_REPORT.md`、`STORY.md`、`CLAIMS_FROM_RESULTS.md`、实验 `results/` 目录
- 用户说「基于这些结果/这个研究方向写论文」

---

## 🔒 证据约束机制（v3 核心）

### Claims-Evidence Matrix（声明-证据矩阵）

规划时建立，每个 claim 必须映射证据：

```markdown
| Claim | Evidence | Status | Section |
|-------|----------|--------|---------|
| 我们方法在 X 上提升 3.2% | results/exp1.json (Ours vs Baseline) | Supported | §4.1 |
| 我们首次解决 Y | 无文献支持 | Unsupported → 弱化 claim | §1 |
```

### GAP_REPORT（证据缺口报告）

对照论文结构槽位 vs 用户实际证据，标记 `covered / partial / missing`：

```markdown
| 结构槽位 | 需要什么 | 用户证据 | 状态 | Slot ID |
|---------|---------|---------|------|---------|
| §4 消融实验 | ablation 矩阵 | 无 | missing | GAP_S4_ABLATION |
| §2 Related | 引用密度 | references.bib 35 条 | partial | GAP_S2_CITES |
```

**硬规则**：缺口就是缺口，**绝不推断/填充/编造证据**；写作时对 missing 槽位输出 `<!-- DATA_NEEDED: GAP_S4_ABLATION — 需补充消融实验数据 -->` 占位。

### 编辑白名单（Edit Whitelist）

审稿修改/换投/生成修订时，可用 YAML 限制可改路径与操作，防止偷偷新增 `\cite`、定理、数字。**协议见 [references/edit-whitelist.md](references/edit-whitelist.md)。**

---

## 🛠️ 可执行脚本

| 脚本 | 用途 | 用法示例 |
|------|------|---------|
| `scripts/fetch_bib.py` | 真实 BibTeX 获取（DBLP→CrossRef）+ bib 卫生校验 | `python scripts/fetch_bib.py fetch "attention is all you need" --author Vaswani --key vaswani2017` / `... clean main.tex references.bib` |
| `scripts/check_tex.py` | 静态 LaTeX 健康检查（未闭合环境/未定义引用/重复label/定理一致性/写作残留/匿名泄漏） | `python scripts/check_tex.py paper/` |

> 首次使用前确认：`python scripts/fetch_bib.py search "test"` 能联网（需可访问 dblp.org / doi.org）。

---

## Agent Rules (Non-Negotiable)

1. **不代写（咨询模式）**：模块提供建议和改进方案，不凭空生成未经用户验证的内容
2. **不编造（全模式）**：永不捏造引用、数据、实验结果；生成模式缺数据写 DATA_NEEDED
3. **保留主导权**：每个修改建议标注为 `[建议]` 类，用户确认后方可应用（生成模式为显式开启的例外）
4. **敏感内容保护**：`\cite{}`、`\ref{}`、数学环境、图表数据永不修改；生成/修改遵循编辑白名单
5. **引用真实**：需要引用时用 `fetch_bib.py` 获取，拉不到标 `[VERIFY]`，绝不幻觉
6. **诚实核对**：声称的性能必须有原始数据支撑；未经审计的数字 claim 不得写入摘要/引言

---

## 参考文档索引

| 文档 | 内容 |
|------|------|
| [workflow-W0-input.md](references/workflow-W0-input.md) | 🆕 生成模式输入契约 |
| [workflow-W1-plan.md](references/workflow-W1-plan.md) | 🆕 Claims-Evidence 规划 + GAP_REPORT |
| [workflow-W2-write.md](references/workflow-W2-write.md) | 🆕 受证据约束的逐节写作 |
| [workflow-W4-compile.md](references/workflow-W4-compile.md) | 🆕 编译校验 + 页数检查 |
| [workflow-W5-audit.md](references/workflow-W5-audit.md) | 🆕 数值 claim 审计 + 引用审计 |
| [workflow-W6-adapt.md](references/workflow-W6-adapt.md) | 🆕 期刊适配 + 润色 + 去 AI |
| [workflow-W7-submit.md](references/workflow-W7-submit.md) | 🆕 Cover Letter + 投稿门禁 |
| [edit-whitelist.md](references/edit-whitelist.md) | 🆕 编辑白名单协议 |
| [venue/ieee.md](references/venue/ieee.md) | 🆕 IEEE 期刊/会议规范 |
| [module-1-structure.md](references/module-1-structure.md) | 结构策略工作流 |
| [module-2-polish.md](references/module-2-polish.md) | 段落润色工作流（7-Pass） |
| [module-3-latex.md](references/module-3-latex.md) | LaTeX 精修工作流 |
| [module-4-journal.md](references/module-4-journal.md) | 期刊适配工作流 |
| [module-5-audit.md](references/module-5-audit.md) | 审稿预检工作流 |
| [module-6-deai.md](references/module-6-deai.md) | 去 AI 痕迹工作流 |
| [module-7-cover-letter.md](references/module-7-cover-letter.md) | Cover Letter 工作流 |
| [module-8-lit-review.md](references/module-8-lit-review.md) | 文献调研与综述 |
| [module-9-citation-check.md](references/module-9-citation-check.md) | 引用验证与格式化 |
| [module-10-thesis.md](references/module-10-thesis.md) | 学位论文写作 |
| [module-11-translation.md](references/module-11-translation.md) | 论文翻译 |
| [polish-prompts.md](references/polish-prompts.md) | 段落润色 Prompt 模板库 |
| [domain-rules/ml-cv-nlp.md](references/domain-rules/ml-cv-nlp.md) | ML/CV/NLP 领域规则 |
| [domain-rules/cs-engineering.md](references/domain-rules/cs-engineering.md) | CS 工程类论文规则 |
| [journal-styles/nature-cns.md](references/journal-styles/nature-cns.md) | Nature/CNS 期刊完整风格指南 |
