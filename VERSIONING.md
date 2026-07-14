# 版本管理约定

## 修改流程

1. 在修改前确认工作区干净，并记录当前宠物 ID、spritesheet SHA-256 和安装目录。
2. 建立一个短分支：`pet/<pet-id>/<change>`。
3. 提交修改前基线，必要时打 `wip/<日期>-before-<change>` 标签。
4. 只修改独立的新宠物 ID；除非用户明确要求，不覆盖已安装旧版。
5. 运行 Hatch Pet 的拆帧、动作预览、方向语义、连续性、单次去色和 `--require-v2` 验证。
6. 提交通过验收的源码与成品，并打 `<pet-id>-v<major>.<minor>.<patch>` 标签。
7. 推送分支和标签到 GitHub；只有完成版本才合并到 `main`。

## 提交信息

- `snapshot: <pet-id> before <change>`：修改前副本。
- `wip: <pet-id> <change>`：可复查但尚未发布的工作进度。
- `release: <pet-id> vX.Y.Z`：全部验收通过的正式版本。
- `qa: <pet-id> <result>`：只更新检测脚本或验收证据。

## 正式发布所需文件

- `<pet>/final/pet.json`
- `<pet>/final/spritesheet-extended.webp`
- `<pet>/final/validation-extended.json`
- `<pet>/qa/chroma-despill-extended.json`
- `<pet>/qa/contact-sheet-extended.png`
- `<pet>/qa/look-directions.png`
- `<pet>/qa/direction-semantics.json`
- `<pet>/qa/look-continuity.json`
- `<pet>/qa/run-summary.json`
