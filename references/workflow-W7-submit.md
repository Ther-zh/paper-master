# 工作流 W7：投稿配套（Cover Letter + 合规）

> 最后一公里。产出投稿所需的外围材料并做提交前门禁。

## Step 1：Cover Letter（→ 模块7）

- 核心贡献 + 创新点 + 与期刊匹配度
- 原创声明、未一稿多投声明、作者确认
- 针对目标期刊定制（IEEE 期刊可能要求说明与会议版的差异）

## Step 2：提交前门禁清单

- [ ] 数值 claim 审计 PASS（W5）
- [ ] 引用审计 PASS（W5）
- [ ] 编译零 ERROR、无未定义引用（W4）
- [ ] 页数合规（W4）
- [ ] 目标 venue 格式完全符合（W6）
- [ ] 匿名/版权声明合规
- [ ] 数据与代码可用性声明（若期刊要求）
- [ ] 补充材料组织完好

## Step 3：交付

```
submit/
├── main.pdf
├── main.tex + sections/ + references.bib
├── cover_letter.txt
├── figures/
├── supp/（补充材料）
└── README_SUBMISSION.md（投稿说明 + 复现指引）
```

> 对数学/理论类投稿，建议同时跑 module-3 的定理一致性检查，确保正文定理与附录证明一一对应。
