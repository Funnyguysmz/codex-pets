# 洛琪希 V2 当前状态

状态：**WIP，未安装，未发布**。

## 已锁定

- 独立 pet ID：`roxy-novel-v2`，不会覆盖 `roxy-novel`。
- 轻小说插画视觉、人物体积与头身比基准。
- V2 后续新生成行使用纯绿 `#00FF00`，最终图集为透明背景。
- 保留用户在任务 `019f5a26-60e1-7620-a562-e8ce778cf053` 中定制的 row 0 待机、row 4 鼠标悬停挥手和 row 7 思考循环。

## 当前阻塞

- `running-right` 最新候选通过结构拆帧与安全边距检查，但视觉 QA 失败：后半周期缺少另一条腿的 passing/rise，末帧提前回到 contact A，播放会猛切后顿一下。
- 四主方向候选的 `090 screen-right` 与 `270 screen-left` 视觉上重复朝左，需要重新生成并再次盲审。
- 因以上两项未通过，当前 `final/` 是旧中间产物，不是 V2 发布件，也没有安装到 Codex。

## 最新 WIP 证据

- `qa/wip/running-right-green-repair-3.png`
- `qa/wip/running-right-green-repair-3-review.json`
- 源图 SHA-256：`8a040e54909302ac87fd641f1fe0525881cdc605f752934a1e86ad70cc2720fb`
