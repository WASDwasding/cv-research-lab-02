# 相邻工作

这些工作出现在「旧书、破损纸页、文档图像」的检索里。任务不是给一本实体书打新旧档。不下载，除非 `open-questions.md` 把题目收成它们的任务。

## 把受损页面修回去

Yang 等. Predicting the Original Appearance of Damaged Historical Documents. arXiv:2412.11634，2024。HDR28K：28552 对图，字符级标注。受损图是在完好页面上合成的缺字、纸张破损和墨迹侵蚀。代码：https://github.com/yeungchenwa/HDR 。输出是修复后的图。

后续有整页修复数据 FPHDR：1633 张房山石经真实图像和 6543 张合成图，损伤分成重、中、轻，但这是字迹损伤等级，不是书的品相。arXiv:2507.05108。

## 污渍去除

StainDoc，arXiv:2410.22922。约 5000 对高分辨率污渍图，污渍是制作出来的，任务是去掉污渍并保住字。另有 StainDoc_Mark、StainDoc_Seal。

## 古籍版面，不是品相

Cheng、Jian、Wu、Jin. SCUT-CAB. ICFHR 2022。4000 张中文古籍，版面元素标注。作者提到页面破损、字迹消退和透背，但标签是版面和阅读顺序。https://github.com/HCIILAB/SCUT-CAB_Dataset_Release

## 二值化竞赛数据

DIBCO 系列和 PHIBD 的任务是把字和背景分开。DCNet 从里面切块做退化分类，见 `2021-arnia-dcnet.md`。

## 没发论文的系统

https://github.com/hyeminLee-project/used_book_grading 。四张图（封面、封底、书脊、书口）加上 YOLOv8 和 Gemini，输出韩文四级：최상、상、중、매입불가。等级是提示词里的规则，不是一篇有划分、有基线的论文，不能当作实验结果。
