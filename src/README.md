# 代码

`env_check.py` 做最小分类训练，用来确认这台机器能跑完。它不读书籍照片，也不输出新旧程度。

依赖：`torch`。装了 `torchvision` 时会尝试 CIFAR-10，否则用合成图。论文壳 `docs/paper/build_shell.py` 另需 `pillow`。

`estimate.py` 是给另一个项目调用的入口：多张书影加原价，返回档、缺陷和估价。模型和价格公式还没定，这三个字段现在是空的，调用方式和以后替换模型时保持一样。做法见 `docs/notes/methods.md`。
