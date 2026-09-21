# 📝 paper-master v3.2

> 一站式学术论文全生命周期写作 Skill — 从研究证据到投稿，双模式（咨询 + 真实写作）

[![Version](https://img.shields.io/badge/version-3.2-blue)]()
[![Modules](https://img.shields.io/badge/modules-13-green)]()
[![Workflow](https://img.shields.io/badge/workflow-W0--W7-orange)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

paper-master v3 是面向 AI Agent（opencode / Claude Code / Codex / Cursor）的学术论文**全生命周期**写作 Skill。v3 从「纯咨询顾问」升级为「**真实写作引擎 + 全流程质检**」。

## 🎭 双模式

| 模式 | 何时用 | 行为 |
|------|--------|------|
| **咨询模式**（默认） | 已有论文草稿需润色/审稿/排版/引用检查 | 输出结构化建议 + `[建议]` 标注，用户确认后修改 |
| **生成模式**（显式） | 「写论文」「从结果生成论文」、传入 NARRATIVE_REPORT | 从证据**真实写作**可编译论文草稿，受证据约束 |

**生成模式铁律**：只写证据支持的内容；缺数据写 `DATA_NEEDED` 占位；引用用 `fetch_bib.py` 真实获取；绝不编造数字/结果/引用。

## 🔄 全生命周期工作流

```
W0 输入契约 → W1 规划(账本+Claims-Evidence+GAP) → W2 生成 → W3 图表 → W4 编译校验
                                                              ↓
W7 投稿 ← W6 适配润色 ← W5 审计(九类数值claim+引用+一致性) ←──┘
```

## 🛠️ 可执行脚本（v3 新增）

| 脚本 | 用途 |
|------|------|
| `scripts/fetch_bib.py` | 真实 BibTeX 获取（DBLP→CrossRef）+ bib 卫生校验（死条目/元数据不一致） |
| `scripts/check_tex.py` | 静态 LaTeX 健康检查（未闭合环境/未定义引用/重复label/定理一致性/写作残留/匿名泄漏） |

## 🧩 13 大模块

| # | 模块 | v3.2 增强 |
|---|------|---------|
| 1 | 结构策略 | Claims-Evidence Matrix + GAP_REPORT + DATA_NEEDED |
| 2 | 段落润色 | Banana Rule 术语一致（术语账本为真源）+ 数值/结论强度保护 |
| 3 | LaTeX 精修 | check_tex.py 静态体检 + 页数/溢出校验 + 定理一致性 |
| 4 | 期刊适配 | IEEE 专项规范 + 系统论文蓝图 |
| 5 | 审稿预检 | 🆕 九类数值 claim 审计 + 一致性审计（机制覆盖/图文码/术语/设计-实现/敏感性）+ 编辑白名单 + 跨模型独立性 |
| 6 | 去 AI 痕迹 | 沿用 |
| 7 | Cover Letter | 沿用 |
| 8 | 文献调研 | 沿用 |
| 9 | 引用验证 | fetch_bib.py 真实获取链 + 引用上下文适切性审计 |
| 10 | 学位论文 | 沿用 |
| 11 | 论文翻译 | 沿用 |
| 12 | 优秀论文对照学习 | 🆕 Oral 蒸馏七项做法 + archetype 指导 + 溯源纪律（快照 external-refs/oral-paper-skill） |
| 13 | 防御性写作阻止 | 🆕 发布会原则 + 12 条规则 + 交稿前 8 问（快照 external-refs/anti-defensive-writing-Skill） |

## 🚀 快速开始

```
# 咨询模式（默认）
帮我润色这段 Abstract
投稿 Nature 前帮我挑毛病
检查我的引用是否都真实存在
对照优秀论文帮我找这篇最值得改进的 3 处
这段结论写得心虚，按发布会原则帮我改

# 生成模式
基于 results/ 和我的实验记录写一篇 ICLR 论文
这是 NARRATIVE_REPORT.md，帮我生成论文全流程
```

## 📁 文件结构

```
paper-master/
├── SKILL.md                          ← 主路由（双模式 + 13 模块 + 工作流）
├── README.md                         ← 本文件
├── scripts/
│   ├── fetch_bib.py                  ← 真实 BibTeX 获取链
│   └── check_tex.py                  ← 静态 LaTeX 健康检查
├── external-refs/                    ← 🆕 外部仓库快照（上游溯源用，运行时无需读取）
│   ├── oral-paper-skill/             ← 883 篇 Oral 摘要蒸馏全量语料（模块12 来源）
│   └── anti-defensive-writing-Skill/ ← CN/EN 双版本（模块13 来源）
└── references/
    ├── workflow-W0-input.md          ← 生成模式输入契约
    ├── workflow-W1-plan.md           ← 账本 + Claims-Evidence 规划 + GAP_REPORT
    ├── workflow-W2-write.md          ← 受证据约束写作（含反防御性写作）
    ├── workflow-W4-compile.md        ← 编译校验 + 页数
    ├── workflow-W5-audit.md          ← 九类数值 claim + 引用 + 一致性审计
    ├── workflow-W6-adapt.md          ← 期刊适配 + 润色 + 防防御复查
    ├── workflow-W7-submit.md         ← 投稿门禁
    ├── ledgers.md                    ← 🆕 三类账本（机制注册表/术语账本/设计-实现差异）
    ├── edit-whitelist.md             ← 编辑白名单协议
    ├── venue/ieee.md                 ← IEEE 期刊/会议规范
    ├── module-1..13*.md              ← 各模块工作流（12=Oral 对照学习，13=防防御性写作）
    ├── polish-prompts.md             ← 润色 Prompt 模板库
    ├── domain-rules/                 ← 领域规则
    └── journal-styles/               ← Nature/CNS 风格
```

## 🔒 核心原则

1. **不代写**（咨询模式）— 提供建议和改进方案，不凭空生成内容
2. **不编造**（全模式）— 永不捏造引用、数据、实验结果；生成模式缺数据写 DATA_NEEDED
3. **保留主导权** — 每个修改标注 `[建议]`，用户确认后应用（生成模式为显式开启的例外）
4. **敏感内容保护** — `\cite{}`、`\ref{}`、数学环境、图表数据永不修改
5. **引用真实** — 用 fetch_bib.py 获取，拉不到标 `[VERIFY]`
6. **诚实核对** — 声称的性能必须有原始数据支撑
7. **反防御不越界**（🆕 v3.1）— 模块13 只调整叙事与措辞，不改变证据真值；必要局限如实保留
8. **账本诚实**（🆕 v3.2）— 机制/术语/实现状态有账可查；`unknown` 不写成已实现，图内文字与正文同取账本

## 📄 License

MIT
