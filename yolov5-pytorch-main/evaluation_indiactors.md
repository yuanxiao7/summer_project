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