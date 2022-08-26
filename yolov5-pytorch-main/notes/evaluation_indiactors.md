7月20日

今天，来谈谈目标检测的评价指标，以下是我个人结合他人的教程写出的理解，如果有误，请及时指出，可以在我的GitHub上issue，我会回复的。

## 四个常用指标

阈值：用来判断先验框的预测的一个值。比如 iou = 0.5

- 注：这里正例指的是有物体的，反例是没有物体的

TP ：当正例被检测大于阈值时他就被认为是有物体的，即，它是正例，模型也把他检测为正例

TN： 当反例被检测大于阈值时他就被认为是有物体的，即，他是反例，但模型把他检测为正例

FN：当正例被检测小于阈值时他就被认为是没有物体的，即，他是正例，但模型把他检测为反例

FN：当反例被检测小于阈值时他就被认为是没有物体的，即，他是反例，模型也把他检测为反例  一般不会用这个值计算

### 混淆矩阵

| 实际  \  预测 |      |      |
| ------------- | ---- | ---- |
|               | 正例 | 反例 |
| 正例          | TP   | FN   |
| 反例          | FP   | TN   |

精确率 等于 检测出正确的正例 除以 检测出正确的例子
$$
precision = TP \div(TP+FN)
$$
召回率 等于 检测出正确的正例 除以 总的正例       查全率 一共有n个正例，检测出多少个正例
$$
recall = TP\div(TP+FP)
$$
准确率 等于 检测正确的例子 除以 总例子
$$
accuracy = (TP+TN)\div(TP+TN+FP+FN)
$$


理论上来说，模型越好，以上的这两个指标的值都比较高，但是由于这两个指标存在一定的矛盾，所以就引入了F1指标来平衡两者。
$$
f1 = (2\times precision\times recall)\div(precision+recall)
$$


### 来论论ap与map

ap是以recall为横坐标，以precision为纵坐标，两指标曲线围成的面积，用于衡量单个类别上的检测效果。

map是相对于整个数据集的，他是所有类别ap的平均值，反映的是整个模型的检测。



<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220720170903784.png" alt="image-20220720170903784" style="zoom:80%;" />

 

<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220720171108490.png" alt="image-20220720171108490" style="zoom:80%;" />

<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220720174343902.png" alt="image-20220720174343902" style="zoom:80%;" />





<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220720174424483.png" alt="image-20220720174424483" style="zoom: 67%;" />





## FPS

FPS是图像领域中的定义，是指画面每秒传输帧数，通俗来讲就是指动画或视频的画面数。FPS是测量用于保存、显示动态视频的信息数量。每秒钟帧数越多，所显示的动作就会越流畅。通常，要避免动作不流畅的最低是30。某些计算机视频格式，每秒只能提供15帧。



## FLOPS

FLOPS（即“每秒[浮点运算](https://baike.baidu.com/item/浮点运算/100607)次数”，“每秒峰值速度”）

是“每秒所执行的[浮点](https://baike.baidu.com/item/浮点)运算次数”（floating-point operations per second）的缩写。

它常被用来估算电脑的执行效能，尤其是在使用到大量浮点运算的[科学计算](https://baike.baidu.com/item/科学计算/10573887)领域中。

正因为FLOPS字尾的那个S，代表秒，而不是[复数](https://baike.baidu.com/item/复数/254365)，所以不能省略掉。

在这里所谓的“浮点运算”，实际上包括了所有涉及[小数](https://baike.baidu.com/item/小数/2172615)的运算。

这类运算在某类应用软件中常常出现，而它们也比整数运算更花时间。

现今大部分的[处理器](https://baike.baidu.com/item/处理器/914419)中，都有一个专门用来处理浮点运算的“[浮点运算器](https://baike.baidu.com/item/浮点运算器/150067)”（[FPU](https://baike.baidu.com/item/FPU/3412317)）。

也因此FLOPS所量测的，实际上就是FPU的执行速度。

而最常用来测量FLOPS的基准程式（benchmark）之一，就是[Linpack](https://baike.baidu.com/item/Linpack)。



## params

模型参数量



## Multi-Add

常常将一个'乘-加'组合视为一次浮点运算，英文表述为'Multi-Add'

理论层面，一般而言，模型的参数量以及flops是否与模型实际的推理速度成反比例的关系

但是flops衡量模型的计算量而不是一个直接衡量模型速度的指标，

模型的并行度，MAC等都会影响推理速度

并行度，模型中的分支计算会带来同步的开销，导致部分kernel闲置，两个flops相同，但是另一个模型中用了很多分支会降低计算的并行度，一般比另一个模型退离时间更长。

还有MAC也就是memory access cost内存使用量，内存访问的时间成本，在cnn中，分组卷积分组数越大，时间成本越高，也会影响推理速度。



**总结：模型的参数量只是一个参考，但不能将它看作反比例关系。**