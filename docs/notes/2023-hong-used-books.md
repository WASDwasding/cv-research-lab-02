# Hong、Jeong 2023：二手书损伤检测

Sumin Hong，Jin Woo Jeong. Automatic Examination of Condition of Used Books with YOLO-Based Object Detection Framework. *Computer Systems Science and Engineering*, 47(2):1611–1632, 2023. DOI:10.32604/csse.2023.038319.

## 问题

二手交易里，品相影响价格，但卖家缺少定量办法。这篇做的是损伤检测，不是把一本书收成一个档。

## 数据

图书馆的书，620 张图，3989 个框。六类：Wear、Spot、Notch、Barcode、Tag、Ripped。

Roboflow 项目 `book_damage_detection`，作者页写 Sumin Hong，CC BY 4.0：https://universe.roboflow.com/sumin-hong/book_damage_detection 。2026-10-14 该页列出 620 张，类别是 Barcode、Notch、Ripped、Spot、Tag，没有 Wear。和论文的六类不一致。下载前再核对当前页面。

## 方法

YOLOv5、YOLOR、YOLOX。增广比较了翻转、旋转、裁剪、mosaic、mixup。输出是框和损伤类，不是品相等级。

## 论文里的数字

YOLOX 在作者最好的训练配置下：mAP@0.5:0.95 为 60.0%，mAP@0.5 为 72.9%。这是检测指标。论文同时写 YOLOX 训练效率最差。这些数字不进本实验主表。

## 边界

作者讨论的是检测是否可行。Barcode 和 Tag 是贴纸，不一定等于「书旧了」。没有整书档位，也没有和卖家品相对照。

## 和本实验

若以后要先找出磨损、污点、撕口，这篇是目前最接近、而且标注能找到的公开材料。它不能直接回答「这本书几成新」。
