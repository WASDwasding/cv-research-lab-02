# 代码

训练与评测脚本放这里。现在只有环境检查。方向锁定、标签规则写死之前，不要堆模型文件。

建议以后：

```
src/
  data/      划分与 Dataset
  models/    骨干与任务头
  train.py
  eval.py
```

依赖写在仓库根目录的 `requirements.txt`。随机种子写进命令行。
