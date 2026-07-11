# 模块 2：段落润色（Paragraph Polish）

> 增强来源：nature-style-writer（855 downloads，7-Pass 编辑法）+ scicomp-research-skills（段落清晰度测试 + 反向大纲 + 声明-证据对齐）

**触发关键词**：润色、改写、paraphrase、academic、polish、学术化、语法修正、句式优化、proofread、proofreading、editing

## 工作流

### 增强版 7-Pass 编辑流程（吸收 nature-style-writer）

```text
Pass 1: Diagnose   — 整体评估：结构、论证链、段落功能、读者友好度
Pass 2: Grammar    — 语法/拼写：时态一致性、冠词、介词、主谓一致
Pass 3: Active     — 被动→主动："We observed" > "It was observed"（Nature 偏好主动态）
Pass 4: Verbs      — 名词化还原："We analyzed" > "We performed an analysis"
Pass 5: Shorten    — 精简冗余：删填充词、合并重复句，每句 ≤30 词
Pass 6: Sharpen    — 锐化断言：精确限定词（suggest/indicate > prove/demonstrate）
Pass 7: Flow       — 段落过渡：确保首句承上、尾句启下、逻辑链连贯
```

### 段落级润色原则（吸收 scicomp-research-skills）

1. **一段一消息**：每次润色聚焦一个段落，不批量处理
2. **首句原则**：每段首句必须明确陈述该段核心观点
3. **句间逻辑**：相邻句之间必须有明确的逻辑关系（因果 / 对比 / 递进 / 例证）
4. **名词自包含**：段落内首次出现的缩写/术语必须定义
5. **声-证对齐**：每个 claim 后面必须紧跟 evidence（数据/引用/推理）

### 段落清晰度测试（吸收 scicomp-research-skills）

润色完毕后，对每一段执行 3 步测试：
1. **外部读者测试**：假装你是第一次读这段，能理解核心观点吗？
2. **反向大纲**：提炼每句话的关键词，检查是否形成逻辑链
3. **补救**：如果测试不通过，加临时小标题和过渡句

## 润色维度

- 🅐 **语法修正**：时态、冠词、介词、主谓一致
- 🅑 **句式优化**：避免头重脚轻、减少冗余从句、句式长短交替（10-25词混合）
- 🅒 **学术语气**：中性客观、避免口语化、控制断言强度
- 🅓 **术语一致性**：同概念用同一术语（首次出现给出缩写定义）
- 🅔 **去冗余**：删 `note that` `it is worth mentioning` `as a matter of fact` 等填充词
- 🅕 **主动化**（🆕）：将不必要的被动语态转为主动语态
- 🅖 **名词化还原**（🆕）：`perform an analysis` → `analyze`；`make a comparison` → `compare`

## 常见学术写作问题修正（吸收 nature-style-writer）

| 问题类型 | 错误示例 | 修正 |
|---------|---------|------|
| 弱动词 | `We carried out an investigation of X` | `We investigated X` |
| 冗余短语 | `due to the fact that` | `because` |
| 过度被动 | `The experiment was performed` | `We performed the experiment` |
| 模糊限定 | `X proves that Y` | `Our results suggest that Y`（除非有因果证据） |
| 过长句 | 40+ 词一句 | 拆分为 2 句 |

## AI 痕迹检测规则（来自 scipilot + 增强）

详见 [polish-prompts.md](polish-prompts.md) 中的 AI 指纹词检测清单。额外增强：
- 检测「delve」「crucial」「notably」「underscores」「pivotal」等 AI 高频词
- 检测「Moreover,」「Furthermore,」「Additionally,」连续使用
- 检测悬垂 -ing 分词 / 过度破折号
- 🆕 检测 `robust` `groundbreaking` `revolutionary` `state-of-the-art` 等过度宣传词
- 🆕 检测连续3句以上相同开头模式（机器写作特征）

## Prompt 模板库

详细 prompt 模板位于 [polish-prompts.md](polish-prompts.md)，包含 6 大类：
- **A 类**：语法修正
- **B 类**：学术化改写
- **C 类**：句式优化
- **D 类**：段落级润色（含反向大纲测试）
- **E 类**：简介/摘要润色
- **F 类**：对比/讨论润色

## 使用优先级

1. 先跑 Pass 1（诊断）— 确定问题类型
2. 再跑 A 类（语法修正） — 基础
3. 跑 Pass 3-4（主动化 + 名词化还原） — Nature 风格
4. 跑 C 类（句式优化）+ Pass 5（精简） — 可读性
5. 跑 B 类（学术化改写）+ Pass 6（锐化） — 专业度 + 精确性
6. 最后跑 D 类（段落润色）+ Pass 7（过渡） — 终极打磨
7. E、F 类按需使用

**重要**：不要一次跑所有 prompt。分步执行，每步验证效果后再进入下一步。

## 🆕 输出格式增强

```
## 润色报告

### 诊断（Pass 1）
- 问题类型：[语法/句式/语气/冗余/学术性]
- 主要问题：[描述]

### 润色后文本
[润色后全文]

### 改动说明
| 行 | 原文 | 改为 | 原因 |
|----|------|------|------|
| 3 | `perform an analysis` | `analyze` | 名词化还原（Pass 4）|
| 5 | `It was observed that` | `We observed` | 主动化（Pass 3）|

### 残余关注
- [仍需人工确认的点]
```

## 与相关模块协作

- → 模块11（翻译）：中译英后自动调用润色
- → 模块6（去AI痕迹）：润色后检查 AI 指纹词
- → [journal-styles/nature-cns.md](journal-styles/nature-cns.md)：Nature 风格参考
