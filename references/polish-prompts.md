# 段落润色 Prompt 模板库

来源：整合自 chatgpt-prompts-for-academic-writing (⭐4,785) 的 "Improving Language and Style" 章节 + scipilot-writing-skill 的去 AI 规则

---

## 类别 A：语法修正

### A1. 基础语法修正
```
Prompt: Correct the grammar of the following text. Only fix grammatical errors (tense, articles, prepositions, subject-verb agreement). Do not change the meaning or writing style.

Text:
[PASTE YOUR PARAGRAPH]
```

### A2. 拼写+语法全面校对
```
Prompt: Act as a language expert. Proofread the following academic text for spelling and grammatical errors. Rewrite it with corrections only — do not change the content, structure, or meaning.

Text:
[PASTE YOUR PARAGRAPH]
```

---

## 类别 B：学术化改写

### B1. 通用学术化
```
Prompt: Rewrite the following paragraph in formal academic English. Use a neutral, objective tone. Avoid colloquialisms, contractions, and informal phrasing. Maintain all technical terms and citations unchanged.

Paragraph:
[PASTE YOUR PARAGRAPH]
```

### B2. 会议论文风格（CS/ML 领域）
```
Prompt: Rewrite this paragraph in the style of a top-tier CS/ML conference paper (e.g., AAAI, ICML, NeurIPS). 
- Be concise and precise
- Use standard technical terminology
- Avoid overhyping claims (no "state-of-the-art" without comparison, no "novel" without justification)
- Keep sentences varied but generally short-to-medium length

Paragraph:
[PASTE YOUR PARAGRAPH]
```

### B3. 被动转主动（适度）
```
Prompt: Review the following academic paragraph. Where appropriate, replace excessive passive voice with active voice while maintaining an objective tone. For CS/engineering papers, active voice is generally preferred for describing our method/contributions.

Paragraph:
[PASTE YOUR PARAGRAPH]
```

---

## 类别 C：句式优化

### C1. 减少冗余
```
Prompt: Review the following text for redundancy and wordiness. Remove filler phrases like "it is worth noting that", "it should be emphasized that", "it is interesting to note that". Shorten long, winding sentences. Output the streamlined version.

Text:
[PASTE YOUR PARAGRAPH]
```

### C2. 句式多样化
```
Prompt: Analyze the sentence structure variety in this paragraph. If too many sentences start the same way or have similar length, rewrite to vary sentence openings and length. Maintain academic tone.

Paragraph:
[PASTE YOUR PARAGRAPH]
```

---

## 类别 D：段落级润色（保留原意的改写）

### D1. Paraphrase（不改变原意）
```
Prompt: Paraphrase the following text using more precise academic and scientific language. Use a neutral tone. Avoid repeating the same words. Do NOT add new information or opinions. Keep all citations intact.

Text:
[PASTE YOUR PARAGRAPH]
```

### D2. 逻辑流增强
```
Prompt: Review this paragraph for logical flow. Check that:
1. The topic sentence clearly states the main claim
2. Each subsequent sentence supports or elaborates on the claim
3. Transitions between sentences are natural (not just "Moreover," "Furthermore,")
Rewrite if needed to improve flow, keeping the original meaning intact.

Paragraph:
[PASTE YOUR PARAGRAPH]
```

---

## 类别 E：简介/摘要润色

### E1. Abstract 优化
```
Prompt: I am writing a paper abstract for [VENUE: AAAI / ICML / NeurIPS]. Please review this abstract and suggest improvements for:
1. Clarity of the problem statement
2. Conciseness of method description
3. Impact of the results claim
4. Appropriate length (typically 150-250 words for CS conferences)

Abstract:
[PASTE YOUR ABSTRACT]
```

### E2. Introduction 首段优化
```
Prompt: Review this introduction opening paragraph. It should follow a "wide → narrow" funnel: broad domain context → specific problem → gap in existing work → our contribution. Suggest improvements.

Paragraph:
[PASTE YOUR PARAGRAPH]
```

---

## 类别 F：对比/讨论润色

### F1. Related Work / Comparison
```
Prompt: Review this related work comparison paragraph. Ensure it:
1. Fairly represents prior work (no strawman)
2. Clearly distinguishes our contribution from existing work
3. Uses appropriate hedging language for claims about others' work
4. Avoids dismissive language like "failed to" or "cannot"

Paragraph:
[PASTE YOUR PARAGRAPH]
```

---

## AI 指纹词检测清单

以下词汇在 AI 生成文本中高频出现，检测到时应标记为潜在 AIGC 痕迹：

**高频 AI 指纹词（需要替换）**：
- delve, delve into
- crucial (过度使用)
- notably
- underscores
- pivotal
- comprehensive
- intricate
- multifaceted
- paramount
- testament (to)
- landscape (领域/图景，AI 最爱)
- realm (领域，AI最爱)
- moreover / furthermore / additionally（连续出现）

**机械句式（需要替换）**：
- "It is worth noting that..."
- "It should be emphasized that..."
- "It is important to highlight that..."
- "This finding underscores the importance of..."
- "...paves the way for future research"

**替换建议**：
| AI 用词 | 推荐替换 |
|---------|---------|
| delve into | examine, investigate, analyze |
| crucial | important, essential, critical |
| notably | in particular, specifically |
| underscores | demonstrates, indicates, suggests |
| pivotal | key, central, important |
| multifaceted | complex, multi-dimensional |
| paramount | essential, vital |
| landscape | area, domain, field |
| Moreover, | [直接进入下句，不需要连接词] |

---

## 使用优先级

1. 先跑 A 类（语法修正）— 基础
2. 再跑 C 类（句式优化）— 提升可读性
3. 再跑 B 类（学术化改写）— 提升专业度
4. 最后跑 D 类（段落润色）— 终极打磨
5. F 类按需使用

**重要**：不要一次跑所有 prompt。分步执行，每步验证效果后再进入下一步。