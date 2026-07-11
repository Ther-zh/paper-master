# CS/工程类学术写作规则

适用于系统、软件工程、数据库、网络、体系结构等 CS 子领域的会议/期刊论文。

---

## 术语规范

### 系统类
| 中文 | 标准英文 |
|------|---------|
| 吞吐量 | throughput |
| 延迟 | latency |
| 可扩展性 | scalability |
| 容错 | fault tolerance |
| 一致性 | consistency |
| 可用性 | availability |
| 分区容忍性 | partition tolerance |
| 加速比 | speedup |
| 基准测试 | benchmark |

### 软件工程类
| 中文 | 标准英文 |
|------|---------|
| 代码库 | codebase |
| 重构 | refactoring |
| 技术债务 | technical debt |
| 回归测试 | regression testing |
| 持续集成 | continuous integration (CI) |
| 部署 | deployment |
| 流水线 | pipeline |

---

## 写作特点

### 与 ML 类论文的核心差异
- **强调系统设计和架构决策**，而非模型性能优劣
- **问题驱动** > 方法驱动："We identify a problem → We design a solution → We evaluate"
- **定性和定量评估并重**：除性能指标还需分析设计权衡
- **更多表格和架构图**：系统论文通常有系统架构图、模块交互图

### 结构模板
1. Introduction：问题 + 观察 + 我们的方案
2. Background/Motivation：举例说明问题有多严重
3. System Design：架构概述 → 各模块详解
4. Implementation：关键实现细节
5. Evaluation：实验设置 → 吞吐量/延迟 → 对比 → 分析
6. Related Work：按问题/方法分类
7. Conclusion

---

## 图表惯例
- 系统架构图：框图和箭头，标注数据流
- 性能图：折线图（x=时间/负载, y=吞吐量/延迟）
- 对比表：多维度对比（功能、性能、复杂度）

## 贡献声明风格
- 强调实际影响力而非理论创新
- 示例："Our system reduces latency by 40% compared to [X] under production workloads."
- 限制声明应诚实："Our approach is limited to read-heavy workloads."