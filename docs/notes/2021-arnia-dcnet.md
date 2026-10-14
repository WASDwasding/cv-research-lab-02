# Arnia、Saddami、Munadi 2021：古籍图像块的退化分类

Fitri Arnia，Khairun Saddami，Khairul Munadi. DCNet: Noise-Robust Convolutional Neural Networks for Degradation Classification on Ancient Documents. *Journal of Imaging*, 7(7):114, 2021. DOI:10.3390/jimaging7070114.

同一组更早的会议论文：Saddami、Munadi、Arnia. Degradation Classification on Ancient Document Image Based on Deep Neural Networks. 用 ResNet101、MobileNetV2、ShuffleNet，在他们的划分上 ShuffleNet 盲测准确率 85%。

## 问题

一张古籍扫描上，退化常常叠在一起，扫描又会带来噪声。先判断这块图像主要是哪一种退化，方便后面的文档分析。不是给书打品相。

## 数据

从 DIBCO 2009–2018、PHIBD 和私有 Jawi 切出 30000 个 224×224 的块。四类各 7500：均匀退化；透背或 show-through；字迹浅或对比度低；涂抹、污渍或斑点。划分 80/10/10。类别是作者从这些二值化数据集里归出来的，不是卖书档位。

## 方法

DCNet 把 MobileNetV2、ShuffleNet、ResNet101 接在一起，并加了一层自转移。训练时看无噪声和加重高斯、散斑噪声两种情况。对照是这三只网络本身，以及 SVM、随机森林。

## 边界

输入是页面上的小块，不是封面、书脊或整本书。四类可以同时出现在一本真正的旧书上，论文仍要求每块一个类。Jawi 那部分不公开。

## 和本实验

只有当我们把任务收成「这一页属于哪类纸张退化」时，DIBCO 和 PHIBD 才用得上。它们不提供九品、良品这种标签。
