# cv-research-lab-02

用图像评估实体书的新旧程度。结果要能接到另一个项目里；能写成论文时按实验记录来写。

已定的范围：看使用品相，输入是多张固定角度的照片，输出是档，再结合原价等估价，实体书不限种类。档的名称和价格公式还没定，见 `docs/notes/open-questions.md`。文献在 `docs/notes/`，四种尚未选定的做法在 `docs/notes/methods.md`。

## 目录

```
docs/notes/     别人的论文、数据集、品相口径
docs/paper/     论文壳。任务锁定前只有节标题
experiments/    以后的实验记录
results/        以后的表和图
src/            env_check.py 检查训练；estimate.py 给另一个项目调用，模型和公式未定时空着返回
data/           图像不进 git
STATUS.md       做到哪一步
```

训练在 4060 游戏本上跑，MacBook 用来在外写代码和文档。分工见 `experiments/README.md`。

环境检查：在仓库根目录运行 `python src/env_check.py`。它只证明训练循环能结束，不读书籍图像。主实验不在 MacBook 上跑。
