# pairwise-hdr-exposure-ghost

## 领域

游戏、图形与多媒体

## 主题

多曝光 HDR 合成

## 说明

运动掩码、噪声阈值与单调色调映射。

初始状态下 `imaging/hdr_exposure_ghost.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
