# 洛琪希 V2 当前状态

状态：**V2 已完成、安装并归档，发布标签 `roxy-novel-v2-v2.0.0`**。

## 已完成

- 独立 pet ID：`roxy-novel-v2`，不会覆盖 `roxy-novel`。
- 轻小说插画风格，保留蓝色双辫、深棕巫师帽、白黑法师服、棕色斗篷、蓝晶法杖与象牙白绑带靴。
- 左右跑步使用完整 8 帧循环，左右脚在周期内交替；左跑由已批准的右跑逐帧镜像得到，人物比例一致。
- 保留任务 `019f5a26-60e1-7620-a562-e8ce778cf053` 中定制的 row 0 待机、row 4 悬停动作和 row 7 思考循环。
- 新跑步源图使用纯绿 `#00FF00`；最终图集为透明背景，没有绿色或洋红色透明残留。
- 16 个观察方向齐全；`090/270` 完整方向帧已作确定性槽位修正，两个主水平方向和上下方向硬门均通过。

## 验证结果

- 最终 WebP SHA-256：`437127c60defbb68c77aa4a457c4e05755cf4fbe56d3b99ddd5e9d342863f67b`
- 图集：1536×2288、8×11、RGBA、`spriteVersionNumber: 2`。
- 洋红键验证：通过，无错误、无警告、透明 RGB 残留 0。
- 绿键验证：通过，无错误、无警告、透明 RGB 残留 0。
- 方向盲测：通过；四个主方向全部通过，少量斜向水平提示较弱，按正常桌面尺寸记为轻微警告，不再追加生成轮次。
- 已安装到 `/Users/mac/.codex/pets/roxy-novel-v2`，安装图集哈希与发布件一致。
- 旧版 `/Users/mac/.codex/pets/roxy-novel` 哈希仍为 `50912170ca1581287a0c9c5cf8f4b4a79c8bbef9a2a5f47bb9cb3f72e62a41f7`，未被覆盖。

## 主要证据

- `final/spritesheet-extended.webp`
- `final/validation-extended.json`
- `final/validation-green-residue.json`
- `qa/contact-sheet-extended.png`
- `qa/look-directions.png`
- `qa/direction-blind-validation.json`
- `qa/cardinal-slot-remap.json`
- `qa/previews/running-right.gif`
- `qa/previews/running-left.gif`
