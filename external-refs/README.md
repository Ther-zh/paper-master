# external-refs · 外部参照快照

本目录存放被 paper-master **吸收为原生能力**的外部 skill 仓库快照（只读参照，运行时无需读取；深挖溯源时才查）。

| 快照 | 上游仓库 | 快照 commit | License | 吸收去向 |
|------|---------|------------|---------|---------|
| `oral-paper-skill/` | [Adkid-Zephyr/oral-paper-skill](https://github.com/Adkid-Zephyr/oral-paper-skill) | `a2c4bc4`（2026-09-20 抓取，当时 174★） | 上游未声明 | [模块12](../references/module-12-oral-learning.md) |
| `anti-defensive-writing-Skill/` | [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) | `102c8b2`（2026-09-20 抓取，当时 1417★） | MIT | [模块13](../references/module-13-anti-defensive.md) |

## 快照说明

- 均为上游 `main` 分支浅克隆快照，已剔除 `.git`（与 `auto-research-skill/external-refs` 约定一致）。
- 快照内 `SKILL.md` 统一改名为 `SKILL.md.off`，**防止运行时把它们注册为独立 skill**（与 external-refs 既有约定一致；上游 README 里的 SKILL.md 链接会因此显示失效，属预期）。
- `oral-paper-skill/` 含完整蒸馏语料（883 篇摘要卡片、21 组 synthesis、pilot 与审核记录、scripts）与其 skill 层（`skills/oral-paper-skill/`）；模块12 只吸收 skill 层的做法与纪律，语料用于溯源。
- `anti-defensive-writing-Skill/` 含 CN/EN 双版本 SKILL（`skills/anti-defensive-writing/SKILL.md.off`、`skills/anti-defensive-writing-en/SKILL.md.off`）与精简提示词。
- 星数/下载量为抓取时原始信号，非质量或维护背书；上游 license 缺失不改变本仓库仅为个人参照用途。

## 更新上游快照

```powershell
git clone --depth 1 https://github.com/Adkid-Zephyr/oral-paper-skill.git tmp-oral
# 对照 diff 后替换本目录快照；若做法有更新，同步修订模块12/13
```
