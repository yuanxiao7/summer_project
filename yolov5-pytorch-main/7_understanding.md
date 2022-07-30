## 池化方式

yolov5博主：https://blog.csdn.net/m0_53392188/article/details/119334634

（7月1日）

### 实例化

**用类创建对象的过程称之为实例化**，**是将一个抽象的概念的类**，**具体到该类实物的过程**。

- 对象名称 = 类名（self， 参数1， 参数2，参数...）括号内为参数列表，可以修改类中的参数，一般python会自动传self，故可以省去。
- 调用这个对象，即，可以调用这个对象与类相关的属性
- 类中设有方法，实例化以后，即可调用方法
- 类可以相互嵌套，即，实例化以后，可以相互调用



### 最大池化

https://blog.csdn.net/weixin_38481963/article/details/109962715  博主写的不错，记住公式就好了

![image-20220702201752438](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220702201752438.png)

### pre_trained

没有显卡或则网络比较大显卡不够，可以冻结训练，或者是有好的数据集，想借用人家已经训练好的网络得到更好的效果。

理解参考：https://blog.csdn.net/gbyy42299/article/details/78977826



(7月7日)

## 常用评价指标

https://www.cvmart.net/community/detail/4992

https://blog.csdn.net/kuweicai/article/details/105082446

https://zhuanlan.zhihu.com/p/58587448

目标检测常用的评价指标有：**交并比**，**准确率**，**精度**，**召回率**，**FPR**，**F1-Score**，**PR曲线-AP值**，**ROC曲线-AUC值**，和**mAP值**和**FPS**。

### 交并比(IOU)

IOU = 两个矩形交集的面积 / 两个矩形并集的面积

![img](https://minio.cvmart.net/cvmart-community/images/202206/30/0/v2-df80b20af4958c0f122d72b766e5cdef_b.jpg)

如上图3-2，假设A是模型检测结果，B为Ground Truth，那么IOU = (A ∩ B) / (A ∪ B)，一般情况下对于检测框的判定都会存在一个阈值，也就是IOU的阈值，一般将IOU值设置为大于0.5的时候，则可认为检测到目标物体。

### 准确率/精度/召回率/F1值/FPR

> True positives (TP,真正): 预测为正,实际为正
> True negatives (TN,真负): 预测为负,实际为负
> False positives(FP,假正): 预测为正,实际为负
> False negatives(FN,假负): 预测为负,实际为正

Accuracy = \frac{TP+TN}{TP+TN+FP+FN} \\$$Precision = \frac{TP}{TP+FP} \\$$Recall = \frac{TP}{TP+FN} \\$$F1-Score = \frac{2\times TP}{2\times TP+FP+FN} \\$$FPR = \frac{FP}{FP+TN} \\

![image-20220707101355856](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220707101355856.png)

![image-20220707101502056](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220707101502056.png)PR曲线-AP值

模型精度，召回率，FPR和F1-Score值无法往往不能直观反应模型性能，因此就有了PR曲线-AP值 和 ROC曲线-AUC值

PR曲线就是Precision和Recall的曲线，我们以Precision作为纵坐标，Recall为横坐标，可绘制PR曲线如下图3-3所示：

![img](https://minio.cvmart.net/cvmart-community/images/202206/30/0/v2-f1ee4f11080634a16a01e3c084896bb6_b.jpg)

**评估标准**：如果模型的精度越高，且召回率越高，那么模型的性能自然也就越好，反映在PR曲线上就是PR曲线下面的面积越大，模型性能越好。我们将PR曲线下的面积定义为AP(Average Precision)值，反映在AP值上就是AP值越大，说明模型的平均准确率越高。

### **ROC曲线-AUC值**

- ROC曲线（Receiver Operating Characteristic）全称：受试者工作特征曲线

- 提到ROC曲线就要先说明一下两个概念：FPR（伪正类率），TPR（真正类率）它们都是对分类任务的一个评测指标。

对于一个二分类任务（假定为1表示正类， 0表示负类），对于一个样本，分类的结果总共有四种：

- 类别实际为1，被分为0，FN（False Negative）
- 类别实际为1，被分为1，TP（True Positive）
- 类别实际为0，被分为1，FP（False Positive）
- 类别实际为0，被分为0，TN（True Negative）

而FPR（False Positive Rate）= FP /（FP + TN），即负类数据被分为正类的比例

TPR（True Positive Rate）= TP /（TP + FN），即正类数据被分为正类的比例

ROC曲线就是RPR和TPR的曲线，我们以FPR为横坐标，TPR为纵坐标，可绘制ROC曲线如下图3-4所示：

![img](https://minio.cvmart.net/cvmart-community/images/202206/30/0/v2-369b745118090a74c2e2403ea7825753_b.jpg)

**评估标准**：

- 当TPR越大，FPR越小时，说明模型分类结果是越好的，反映在ROC曲线上就是ROC曲线下面的面积越大，模型性能越好。我们将ROC曲线下的面积定义为AUC(Area Under Curve)值，反映在AUC值上就是AUC值越大，说明模型对正样本分类的结果越好。



### **mAP**

- Mean Average Precision(mAP)是平均精度均值，具体指的是不同召回率下的精度均值。在目标检测中，一个模型通常会检测很多种物体，那么每一类都能绘制一个PR曲线，进而计算出一个AP值，而多个类别的AP值的平均就是mAP。

#### **评估标准**：

- mAP衡量的是模型在所有类别上的好坏，属于目标检测中一个最为重要的指标，一般看论文或者评估一个目标检测模型，都会看这个值，这个值(0-1范围区间)越大越好。

#### **划重点！！！**

- 一般来说mAP是针对整个数据集而言的，AP则针对数据集中某一个类别而言的，而percision和recall针对单张图片某一类别的。



### EPPI-MR

#### 	MR    

- 漏检率，即 MR = 1 - recall  越小越好

#### 	FPPI

- 每张图片的误检率，  fppi = fp /n    fp误检数    n照片总数

- MR-2  是以fppi为下x坐标，以log（MR）为y坐标，均取[0.01, 1]范围内的9个fppi的其对应的9个log（MR）的值，并对这几个y坐标值 取平均，最后通过指数运算恢复MR的百分比形式（可能是小数形式），就获得MR-FPPI的曲线，MR-2指标越小越好





###  FPS

Frame Per Second(FPS)指的是模型一秒钟能检测图片的数量，不同的检测模型往往会有不同的mAP和检测速度，如下图3-5所示：

![图3-5.不同模型的准确率与检测速度](https://minio.cvmart.net/cvmart-community/images/202206/30/0/v2-4349d4587ebb9fbd7c6daaf5640c4d6e_b.jpg)

目标检测技术的很多实际应用在准确度和速度上都有很高的要求，如果不计速度性能指标，只注重准确度表现的突破，其代价是更高的计算复杂度和更多内存需求，对于行业部署而言，可扩展性仍是一个悬而未决的问题。因此在实际问题中，通常需要综合考虑mAP和检测速度等因素。参考**目标检测中的评价指标有哪些[25]**



## 存在的六大难点与挑战

每一个检测任务都有其特有的检测难点，比如背景复杂，目标尺度变化大，颜色对比度低等挑战，这就导致某个检测算法在检测任务A上可能表现SOTA，但在检测任务B上表现得可能不尽如人意。因此，分析研究每一个检测任务存在的难点与挑战至关重要，这有利于我们针对不同的检测难点设计出不同的技术以解决该项问题，从而使得我们提出的算法能够在特定的任务上表现SOTA。

我们对大部分检测任务加以分析，概括出了以下几点在检测任务可能存在的检测难点与挑战:

1. **待检测目标尺寸很小，导致占比小，检测难度大**
2. **待检测目标尺度变化大，网络难以提取出高效特征**
3. **待检测目标所在背景复杂，噪音干扰严重，检测难度大**
4. **待检测目标与背景颜色对比度低，网络难以提取出具有判别性的特征**
5. **各待检测目标之间数量极度不均衡，导致样本不均衡**
6. **检测算法的速度与精度难以取得良好平衡**





## 网络预处理后处理

### 预处理

- 数据集的导入、划分、打包

### 前处理

- 从划分好的数据集里，导入图片，转换图片数据类型
- 对图片进行resize
- 对图片进行数据增强
- 将处理好的图片送进网络

### 后处理

- 在模型完成预测之后的处理
- 如yolov5，他根据与之检测出的框可能会有重叠的，进行非极大抑制等





Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.937, 0.999)
    eps: 1e-08
    lr: 2.9999999999999997e-05
    maximize: False
    weight_decay: 0

Parameter Group 1
    amsgrad: False
    betas: (0.937, 0.999)
    eps: 1e-08
    lr: 2.9999999999999997e-05
    maximize: False
    weight_decay: 0

Parameter Group 2
    amsgrad: False
    betas: (0.937, 0.999)
    eps: 1e-08
    lr: 2.9999999999999997e-05
    maximize: False
    weight_decay: 0
)
