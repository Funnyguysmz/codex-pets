# Codex Animated Pets

这个私有仓库保存 Codex 桌面宠物的可回退版本、Hatch Pet 源资料和验收记录。

## 当前宠物

| 目录 | 状态 | 说明 |
| --- | --- | --- |
| `roxy-novel-v1/` | 已安装基线 | 当前 `roxy-novel` 的只读快照，不在 V2 修复中覆盖 |
| `roxy-novel-v2/` | 已发布并安装 | 独立 ID `roxy-novel-v2`；发布标签 `roxy-novel-v2-v2.0.0`，旧版未覆盖 |

## 发布原则

- 每次用户要求修改前，先提交修改前快照；修改完成后再提交验收结果。
- WIP 只使用 `wip/<日期>-<说明>` 标签；通过 Hatch Pet 全部验收后使用 `<pet-id>-v<版本号>` 正式标签。
- 正式宠物必须包含 `pet.json`、`spritesheet.webp`、验证 JSON、去绿报告和最终 QA 图。
- 旧版本只增加新提交和标签，不覆盖历史文件，也不强制改写 Git 历史。
- 临时拆帧、失败生成缓存和可重复生成的中间文件不进入仓库；关键失败证据放在各宠物的 `qa/wip/`。

详见 [VERSIONING.md](VERSIONING.md)。

当前正式版本：`roxy-novel-v2-v2.0.0`，图集 SHA-256 为 `437127c60defbb68c77aa4a457c4e05755cf4fbe56d3b99ddd5e9d342863f67b`。
