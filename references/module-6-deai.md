# 模块 6：去 AI 痕迹（De-AI）

**触发意图**：「去 AI 味」「检测 AI 痕迹」「humanize」「像人写的」

## 工作流

1. 扫描全文，检测以下 AIGC 指纹：
   - **高频 AI 词汇**：delve, crucial, notably, underscores, pivotal, comprehensive, intricate, multifaceted, paramount, testament
   - **机械连接词堆叠**：Furthermore, Moreover, Additionally, In addition
   - **模板化转折句**：「It is worth noting that...」「It should be emphasized that...」
   - **空泛归因**：「Many studies have shown...」未给具体引用
   - **过度使用破折号**解释
2. 标注严重程度（需改 / 建议改 / 可忽略）
3. 对需改项提供人工化改写建议

## AI 指纹词替换表

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

完整的 AI 指纹词检测清单见 [polish-prompts.md](polish-prompts.md) 末尾「AI 指纹词检测清单」章节。