# Paper-Master

一站式学术论文写作 Skill，覆盖从初稿到投递的全流程。无需选择子技能——只需描述你要做什么，paper-master 自动路由到对应模块。

## 触发条件

当用户提到以下任一场景时激活本 Skill：
- 论文写作、论文润色、论文格式、论文结构
- LaTeX 论文、会议论文、期刊论文、AAAI/ICML/NeurIPS/CVPR/IEEE/ACM
- 语法检查、学术写作、英文润色
- 去AI痕迹、AI检测、humanize
- 审稿人视角、投稿前检查、cover letter
- 期刊风格适配、目标期刊、换投

## 核心架构

paper-master 采用**智能路由**设计：根据用户意图自动选择以下 7 个模块中的 1 个或多个执行。

## 7 大功能模块

### 模块 1：结构策略（Structure Strategist）
**触发意图**：「规划论文结构」「帮我梳理逻辑」「IMRAD 结构」「实验放哪一节」

**工作流**：
1. 分析用户提供的论文内容或研究主题
2. 按 IMRAD (Introduction / Methods / Results / Discussion) 标准检查结构
3. 输出：分节建议 + 各节核心论点清单 + 逻辑流检查
4. 与 AAAI/目标会议格式要求对齐

**质量检查点**：
- 每节是否有明确的「claim - evidence - analysis」三角
- Introduction 是否从宽到窄（领域 → 问题 → gap → contribution）
- Results 与 Method 是否一一对应

---

### 模块 2：段落润色（Prompt Polish）
**触发意图**：「润色这段话」「帮我改改表达」「学术化改写」「paraphrase」

**工作流**：
1. 分析输入文本的问题类型（语法 / 句式 / 语气 / 冗余 / 学术性）
2. 从 `references/polish-prompts.md` 中匹配最佳润色策略
3. 根据上下文自动选择 prompt 模板
4. 输出：润色后的文本 + 改动说明（结构化 diff）

**润色维度**：
- 🅐 语法修正：时态、冠词、介词、主谓一致
- 🅑 句式优化：避免头重脚轻、减少冗余从句、提升可读性
- 🅒 学术语气：中性客观、避免口语化、控制断言强度
- 🅓 术语一致性：同概念用同一术语
- 🅔 去冗余：删「note that」「it is worth mentioning」等填充词

**AI 痕迹检测规则**（来自 scipilot）：
- 检测「delve」「crucial」「notably」「underscores」「pivotal」等 AI 高频词
- 检测「Moreover,」「Furthermore,」「Additionally,」连续使用
- 检测悬垂 -ing 分词
- 检测过度使用破折号

---

### 模块 3：LaTeX 精修（LaTeX Polish）
**触发意图**：「检查我的 LaTeX」「编译报错」「格式不对」「图表排版」

**工作流**：
1. 读取 `.tex` 文件
2. 分节提取文本内容（使用 parser 逻辑）
3. 按粗→细顺序检查：
   - 编译级：缺失的 `\end{}`、未定义的引用、错误环境嵌套
   - 格式级：图表标签位置、浮动体参数、公式编号
   - 样式级：引用格式、断词、跨页孤行
4. 输出带位置标注的修改建议

**安全规则**（永不碰的内容）：
- `\cite{}`、`\ref{}`、`\label{}` 内部
- 数学环境 `$...$`、`$$...$$`、`\begin{equation}...\end{equation}` 内部
- 已注释的行（以 `%` 开头）

---

### 模块 4：期刊适配（Journal Adapt）
**触发意图**：「帮我适配 AAAI 风格」「换成 ICML 格式」「这个期刊怎么写」

**工作流（两阶段）**：

**Phase 1 — 风格分析**：
1. 用户提供 3-5 篇目标期刊/会议已发表论文
2. 提取各论文的 Style Card（10 维度：摘要结构、引言架构、贡献表达、文献综述方式、方法论描述、结果呈现、讨论风格、语言特点、缺失模式、特色亮点）
3. 聚合生成目标期刊的 Journal Style Card

**Phase 2 — 逐节修改**：
1. 按 Abstract → Introduction → Related Work → Method → Experiments → Conclusion 顺序
2. 每节输入用户手稿 → 对比 Journal Style Card → 输出修订建议
3. 提供「风格差异报告」：列出与目标期刊不一致之处

**内置领域静态规则**（位于 `references/domain-rules/`）：
- `ml-cv-nlp.md`：ML/CV/NLP 领域术语表、公式排版惯例、评测指标写法
- `cs-engineering.md`：CS 工程类论文风格

---

### 模块 5：审稿预检（Pre-Review Audit）
**触发意图**：「投稿前检查」「审稿人会不会觉得」「帮我挑毛病」

**工作流**：
1. 从四个视角独立审读论文：
   - **方法学审稿人**：研究设计、统计严谨性、可重复性
   - **领域审稿人**：文献覆盖、理论框架、相关工作对比
   - **批判审稿人**：逻辑谬误、过度声称、证据链薄弱处
   - **语言审稿人**：拼写错误、语法问题、术语不一致
2. 合成审稿意见 → 生成 Red Flag 清单 + 修改优先级
3. 输出：分问题的严重程度（Critical / Major / Minor / Suggestion）

---

### 模块 6：去 AI 痕迹（De-AI）
**触发意图**：「去 AI 味」「检测 AI 痕迹」「humanize」「像人写的」

**工作流**：
1. 扫描全文，检测以下 AIGC 指纹：
   - 高频 AI 词汇（delve, crucial, notably, underscores, pivotal, comprehensive, intricate, multifaceted, paramount, testament）
   - 机械连接词堆叠（Furthermore, Moreover, Additionally, In addition）
   - 模板化转折句（「It is worth noting that...」「It should be emphasized that...」）
   - 空泛归因（「Many studies have shown...」未给具体引用）
   - 过度使用破折号解释
2. 标注严重程度（需改 / 建议改 / 可忽略）
3. 对需改项提供人工化改写建议

---

### 模块 7：Cover Letter 生成
**触发意图**：「写投稿信」「cover letter」「submission letter」

**工作流**：
1. 从论文中提取关键信息：核心贡献、创新点、与期刊匹配度
2. 生成符合目标会议/期刊格式的 Cover Letter
3. 检查合规项：原创声明、未一稿多投声明、作者确认

---

## 路由规则

| 用户意图关键词 | 路由模块 | 优先级 |
|-------------|---------|--------|
| 润色/改写/paraphrase/academic language | 模块2：段落润色 | P1 |
| LaTeX/编译/格式/图表/.tex | 模块3：LaTeX精修 | P1 |
| 结构/逻辑/IMRAD/规划/写哪 | 模块1：结构策略 | P2 |
| 适配/风格/目标期刊/AAAI/ICML | 模块4：期刊适配 | P2 |
| 审稿/挑毛病/投稿前/检查/audit | 模块5：审稿预检 | P3 |
| 去AI/AI痕迹/humanize/像人写的 | 模块6：去AI痕迹 | P3 |
| cover letter/投稿信 | 模块7：Cover Letter | P3 |

**组合路由**：当用户意图涉及多个模块时，按如下顺序执行：
1. 结构策略 → 2. 段落润色 → 3. LaTeX精修 → 4. 去AI痕迹 → 5. 审稿预检 → 6. 期刊适配 → 7. Cover Letter

## AAAI 场景默认配置

当检测到用户论文为 AAAI 投稿（如存在 `aaai2027.sty` 或用户提及）时，自动加载以下默认行为：
- 双栏格式检查（`\documentclass[letterpaper]{article}` 风格）
- 页数限制提醒（AAAI 2027 通常 7页正文 + 额外页）
- 匿名化检查（`\author{}` 应为 `Anonymous Submission`）
- 引用格式检查（`aaai2027.bst`）

## 注意事项

1. **不代写**：模块提供建议和改进方案，不凭空生成未经用户验证的内容
2. **不编造**：永不捏造引用、数据、实验结果
3. **保留主导权**：每个修改建议标注为 `[建议]` 类，用户确认后方可应用
4. **敏感内容保护**：`\cite{}`、`\ref{}`、数学环境、图表数据永不修改