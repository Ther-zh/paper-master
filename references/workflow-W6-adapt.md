# 工作流 W6：适配与润色（期刊风格 + 7-Pass + 去 AI）

> 审计通过后，针对目标期刊/会议做风格适配和最终润色。

## Step 1：期刊风格适配（→ 模块4）

- 明确目标 venue（Nature/AAAI/ICML/NeurIPS/CVPR/IEEE/ACM...）
- 加载对应风格：`journal-styles/nature-cns.md`、`venue/ieee.md`（🆕 IEEE 专项）
- 逐节对比 Journal Style Card，输出「风格差异报告」

## Step 2：段落润色（→ 模块2）

- 7-Pass 编辑法（Diagnose→Grammar→Active→Verbs→Shorten→Sharpen→Flow）
- 保持声明强度与证据匹配（Pass 6 用 suggest/indicate 而非 prove/demonstrate）
- Banana Rule：术语全文一致

## Step 3：去 AI 痕迹（→ 模块6）

- 扫描 AI 高频词与机械句式
- 替换为人工化表达

## Step 4：最终一致性检查

- [ ] 引用/图表/公式交叉引用全部有效
- [ ] 术语/缩写全文一致
- [ ] 页数符合 venue 限制
- [ ] 匿名合规（若需）
- [ ] 无 `[VERIFY]` / DATA_NEEDED 残留

→ 下一阶段: [W7 投稿](workflow-W7-submit.md)
