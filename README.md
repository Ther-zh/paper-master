# 📝 paper-master v2

> 一站式学术论文写作 Agent Skill — 集 40+ 开源技能之所长

[![Version](https://img.shields.io/badge/version-2.0-blue)]()
[![Modules](https://img.shields.io/badge/modules-11-green)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

paper-master 是面向 AI Agent（Claude Code / Codex / Cursor）的学术论文写作 Skill。从**文献调研**到**投稿 Cover Letter**，覆盖论文写作全流程。v2 版本吸收了 Nature Skill 生态、scicomp-research-skills、citation-verifier 等 40+ 个开源技能的方法论精华。

---

## 🚀 快速开始

激活 paper-master 后，直接描述你的需求：

```
帮我润色这段 Abstract
投稿 Nature 前帮我挑毛病
帮我做这个方向的文献综述
检查我的引用是否都真实存在
帮我规划博士论文结构
```

Skill 会自动路由到对应模块，输出结构化建议。

---

## 🧩 11 大模块

| # | 模块 | 触发场景 | 来源 |
|---|------|---------|------|
| 1 | **结构策略** | 论文结构规划、IMRAD 组织 | 原有 |
| 2 | **段落润色** | 润色、改写、学术化表达 | 🆕 Nature 7-Pass 编辑法 |
| 3 | **LaTeX 精修** | 编译错误、格式、图表排版 | 🆕 出版级图表规范 |
| 4 | **期刊适配** | 适配目标期刊/会议风格、换投 | 🆕 Nature/CNS 风格库 |
| 5 | **审稿预检** | 投稿前检查、模拟审稿 | 🆕 对抗性自审 + 声明-证据对齐 |
| 6 | **去 AI 痕迹** | 降低 AI 检测率、humanize | 原有 |
| 7 | **Cover Letter** | 投稿信撰写 | 原有 |
| 8 | **文献调研** 🆕 | 文献搜索、综述写作、PRISMA 流程 | scicomp + SLR 方法论 |
| 9 | **引用验证** 🆕 | DOI 验证、引用真实性、BibTeX 格式 | citation-verifier |
| 10 | **学位论文** 🆕 | 硕博论文、开题、盲审、答辩 | dissertation-workflow |
| 11 | **论文翻译** 🆕 | 中英互译、术语一致性 | arxiv-translator |

---

## 🎯 特色能力

### Nature 7-Pass 编辑法
吸收 nature-style-writer（855 downloads）的分层编辑流程：
```
Diagnose → Grammar → Active → Verbs → Shorten → Sharpen → Flow
```

### 出版级图表规范
吸收 nature-figure（975 downloads）的图表设计标准：
- 色盲友好配色方案
- matplotlib 出版级 rcParams
- 图表自明性检查

### 对抗性自审
吸收 scicomp-research-skills 的审稿方法论：
- 假装竞争对手找出最弱 3 点
- 为每个 claim 建立证据映射
- Nature 审稿人 5 维评估框架

### 声明-证据对齐
每个 major claim 必须有对应的数据/引用/推理支撑，标记无证据的 bare claim。

---

## 📁 文件结构

```
paper-master/
├── SKILL.md                         ← 主路由（11模块 + 智能路由）
├── SKILL-v0-backup.md               ← 旧版备份
├── README.md                        ← 本文件
├── references/
│   ├── module-1-structure.md        ← 结构策略
│   ├── module-2-polish.md           ← 🆕 段落润色（Nature 7-Pass）
│   ├── module-3-latex.md            ← 🆕 LaTeX 精修（图表规范）
│   ├── module-4-journal.md          ← 🆕 期刊适配（风格库）
│   ├── module-5-audit.md            ← 🆕 审稿预检（对抗性自审）
│   ├── module-6-deai.md             ← 去 AI 痕迹
│   ├── module-7-cover-letter.md     ← Cover Letter
│   ├── module-8-lit-review.md       ← 🆕 文献调研
│   ├── module-9-citation-check.md   ← 🆕 引用验证
│   ├── module-10-thesis.md          ← 🆕 学位论文
│   ├── module-11-translation.md     ← 🆕 论文翻译
│   ├── polish-prompts.md            ← 润色 Prompt 模板库
│   ├── domain-rules/
│   │   ├── ml-cv-nlp.md             ← ML/CV/NLP 领域规则
│   │   └── cs-engineering.md        ← CS 工程类论文规则
│   └── journal-styles/
│       └── nature-cns.md            ← 🆕 Nature/CNS 完整风格指南
└── scripts/                         ← 辅助脚本
```

---

## 📚 知识来源

paper-master v2 从以下开源项目中吸收了方法论精华：

| 来源 | 认可度 | 吸收内容 |
|------|--------|---------|
| nature-style-writer | 855 downloads | Nature 7-Pass 编辑法 |
| nature-figure | 975 downloads | 出版级图表规范、色盲配色 |
| nature-paper-reviewer | ClawHub | Nature 审稿人 5 维评估框架 |
| scicomp-research-skills | 8⭐ GitHub | 段落清晰度测试、反向大纲、对抗性自审 |
| citation-verifier | 42 installs | DOI 验证、引用真实性检查 |
| dissertation-workflow-core | 29 installs | 学位论文全流程 |
| arxiv-translator | 426⭐ | 逐段翻译流程、术语维护 |
| systematic-literature-review | 21 installs | PRISMA 文献筛选流程 |
| awesome-latex-skills | 172⭐ | LaTeX 错误诊断速查表 |
| AI-Research-SKILLs | 10.6K⭐ | ML 论文特有结构规范 |
| paper-master-opt | 本地 | 歧义处理、检查点机制、换投路由 |

> 完整发现报告见 `aha-skills-finder/runs/paper-writing-discovery/`

---

## 🔒 核心原则

1. **不代写** — 提供建议和改进方案，不凭空生成内容
2. **不编造** — 永不捏造引用、数据、实验结果
3. **保留主导权** — 每个修改标注为 `[建议]`，用户确认后应用
4. **敏感内容保护** — `\cite{}`、`\ref{}`、数学环境、图表数据永不修改

---

## 🛠️ 安装

将 `paper-master/` 目录放在你的 skills 路径下即可。Agent 会根据 `SKILL.md` 中的触发条件自动激活。

---

## 📄 License

MIT