# cv-research-lab-02

用图像评估实体书的新旧程度。能写成论文时按实验记录来写。

已定的范围：看使用品相，输入是六张固定角度的照片，输出是档，再结合原价等估价，实体书不限种类。做法是六张图一起做有序分类。必拍、标注和三批书的本数在 `experiments/label_protocol.md` 第 6 节。还没定死的阈值和价格系数见 `docs/notes/open-questions.md`。

## 目录

```
docs/notes/     别人的论文、数据集、品相口径
docs/paper/     论文壳。任务锁定前只有节标题
experiments/    以后的实验记录
results/        以后的表和图
src/            env_check.py 检查训练；estimate.py 根据书影和原价返回档与估价，模型未训练时空着返回
data/           图像不进 git
STATUS.md       做到哪一步
```

训练在 4060 游戏本上跑，MacBook 用来在外写代码和文档。分工见 `experiments/README.md`。

环境检查：在仓库根目录运行 `python src/env_check.py`。它只证明训练循环能结束，不读书籍图像。主实验不在 MacBook 上跑。
