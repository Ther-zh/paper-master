# ML/CV/NLP 领域学术写作规则

适用于 AAAI / ICML / NeurIPS / CVPR / ACL / EMNLP 等会议论文。

---

## 术语规范

### 常用术语
| 中文 | 标准英文 | 禁止写法 |
|------|---------|---------|
| 准确率 | accuracy | accurate rate |
| 精确率 | precision | precise rate |
| 召回率 | recall | recall rate |
| F1分数 | F1-score | F1 score / f1 measure |
| 主干网络 | backbone | backbone network |
| 消融实验 | ablation study | ablation experiment |
| 基线 | baseline | basic line |
| 数据集 | dataset | data set |
| 超参数 | hyperparameter | hyper-parameter |
| 微调 | fine-tune / fine-tuning | fine tune |
| 预训练 | pre-train / pre-trained | pretrain |
| 推理 | inference | reasoning (推理=哲学) |
| 嵌入 | embedding | embedding vector |
| 特征图 | feature map | feature graph |
| 损失函数 | loss function | lost function |

### 评测指标写法
- 百分比：`85.3%`（不要写 `0.853`）
- 标准差：`85.3 ± 2.1%`
- p值：`p < 0.05`
- 表格加粗最佳结果

---

## 论文结构惯例

### Abstract
- 长度：150-250 词（AAAI/ICML/NeurIPS 硬限）
- 结构：问题 → 挑战 → 方法要点 → 关键结果
- 禁止：引用、公式、缩写（除非广为人知如 CNN, LLM）

### Introduction
- 漏斗结构：领域背景(2-3句) → 具体问题(2-3句) → 已有方法局限(2-3句) → 我们的贡献(3-4句)
- 最后一句话应明确列出贡献（3点为佳）
- 示例贡献句式：
  - "We propose [METHOD], which..."
  - "We conduct extensive experiments on [DATASETS], showing..."
  - "Our analysis reveals that..."

### Related Work
- 按主题分小节（不是按时间顺序）
- 每个小节结束时说明与我们的区别
- 避免贬低前人工作（不要用 "fails to" / "cannot"）
- 推荐句式："While [PRIOR] achieves [X], it does not address [Y], which is the focus of our work."

### Method
- 按逻辑顺序（不是实验顺序）
- 先给 overview 图/段
- 公式编号只给关键公式
- 算法伪代码放在最后（如果空间够）

### Experiments
- 主表：SOTA 对比表
- 消融：证明每个组件的有效性
- 分析：可视化、case study、错误分析
- 计算资源声明（部分会议要求）

### Conclusion
- 不重复 Abstract
- 总结贡献（2-3句）
- 指出限制与未来方向（1-2句）

---

## 写作风格

### 时态
- Introduction/Related Work：现在时（描述已知事实）
- Method：现在时（描述我们的系统）
- Experiments：过去时（描述已做实验）
- Results：现在时（描述表中结果）/ 过去时（描述观察过程）
- Conclusion：现在时

### 人称
- "we" / "our" 完全可接受（CS 领域惯例）
- 避免："the authors" / "this paper" 作主语（更自然用 "we"）

### 断言强度
- 强声明（需充分证据）：显著优于 / outperform / state-of-the-art
- 中声明：achieve competitive results / comparable to
- 弱声明：show promising results / suggest that
- 避免：过度推销（"revolutionary" / "first ever"）

---

## 公式排版

- 只给关键公式编号
- 符号一致性：全文用同一符号
- 标量小写斜体 (a), 向量小写粗体 (𝐱), 矩阵大写粗体 (𝐖)
- 损失函数用 ℒ 或 L
- 引用公式：Eq. (1) / Equation 1

## 图表

- 图表标题在表上方、图下方
- 表用三线表
- 图向量格式：PDF > EPS > PNG
- 图表必须在正文中被引用（"Figure 1 shows..."）
- 避免 "Fig." / "Tab." 缩写（视会议规定）