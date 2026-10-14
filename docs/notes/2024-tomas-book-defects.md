# Tomas 等 2024：书缺陷检测

John Paul Tomas，Katrice Asher Albano，Jill Samantha Alday，Matthew Raphael Corbe，Gian Nicole Pangan. Using YoloV8 Book Defect Detection Model with MIRNet LLI. WCSE 2024，pp. 27–35。PDF：https://www.wcse.org/WCSE_2024/005.pdf

## 问题

在个人藏书照片上检测缺陷。品相档（如 Ex-Library、Like New、Good）被写成检测做好之后的下一步，这篇没有做。

## 数据

个人藏书。每本至少 5 个角度：封面俯视、封底俯视、书脊俯视、封面加切口的 45 度、内页。白底，顶光。内页可以多张。合计 531 张：训练 372、验证 107、测试 52。标签参照 AbeBooks 的旧书用语，十类：Chip、Spot（文中对应 foxing）、Crease、Tear、Stain、Nick、Mark、Annotations、Barcode、Label。

文中写数据在 Roboflow 上。没有给出可长期引用的项目地址，不把这 531 张当成已公开数据。

类别数量不平衡。文中点名偏多的有 Spot 347、Crease 302、Stain 276、Chip 260；偏少的有 Barcode 67、Label 62、Nick 62、Tear 56、Mark 48。Annotations 162。这些是标注条数，不是图像数。

## 方法

图先标注，再用 MIRNet 做低光增强，框的位置沿用原标注。比较了原 10 类和合并后的类（Barcode+Label，Mark+Nick，Chip+Tear），以及 Roboflow 3.0 检测器和 YOLOv8。图像缩到 640×640。

## 论文正文里的数字

第 4 节：Roboflow 3.0、原始标签，mAP 从 0.10 到加 MIRNet 后的 0.11；YOLOv8 的 mAP 保持 0.07。作者认为低光增强的收益很小，合并类别也没有明显拉高指标，并在建议一节写整体表现差。PDF 里的表排版乱，上面的数按第 4 节正文，不按表重算。不进本实验主表。

## 边界

拍摄条件单一。缺陷类很多、样本少。模型没有输出档位。低光增强是在标注之后做的，作者自己也说也许该在标注之前做。

## 和本实验

有用的是拍摄角度和十个类的定义，以及「检测不等于档位」这件事。0.07–0.11 的 mAP 说明，即使用了和卖书术语对齐的类，小数据上的检测也可以几乎不可用。
