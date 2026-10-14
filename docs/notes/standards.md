# 别人用过的品相口径

这些是市场上的说法，不是本实验已经选定的标签。选定之前不写进 `experiments/`，也不写进论文方法。

## AbeBooks / ABAA

档从好到差大致是：New、As New、Fine、Near Fine、Very Good、Good、Fair、Poor。书和护封可以分开打，写成 `VG/G` 这种形式。AbeBooks 检索接口用 `bookcondition=` 过滤，取值包括 new、asnew、fine、nearfine、verygood、good、fair、poor。接口返回的是卖家填写的品相，不是从图像算出来的。

NMLP 把 AB Bookman、eBay、AbeBooks 的用词对照成一张表，并给了机器可读的 `condition-standard.json`（页面写 CC BY 4.0）：https://newmexicoliteracyproject.org/book-condition-standard 。这是口径对照，不是图像数据集。

## 中文旧书的「品」

流通说法里，十品接近全新、无缺页、无他人墨迹；九品允许封面和书角轻度自然磨损；往下到八品、七品、六品，污迹、折角、笔迹、破损逐渐加重。六品以下常被说成没有收藏价值。同一套说法还有「自然旧」：没怎么翻，但纸自己黄了。

这套口径把使用痕迹和纸张变旧拆开了。本实验还没决定要不要拆。

## 多抓鱼

公开说明里，售卖侧是全新、良品、中品。良品是轻微使用痕迹；中品是明显使用痕迹，或无法修复的瑕疵。收购侧另有品相良好、品相中等、品相不合格：中等比良好收购价低 20%，不合格拒收。这是平台规则，不是带图的公开数据集，也不是本实验的标签。
