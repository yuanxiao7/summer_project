# 改动对比



## 改动一、激活函数



### 说明

此次改动训练了两次。

- 主要无关变量 batch_size、精度、num_works等

- 自变量  激活函数

- 指标为所有类的平均指标，指标是由测试脚本检测而来的。



### baseline_SiLU

baseline使用的是SiLU函数，即swish函数，除了计算量比较高以外，她所获得的激活效果是非常好的，以至于v6，v7的激活函数依旧是他，此次是从零开始训练的baseline模型，其中train的loss由2.7左右下降到0.057左右，val的loss由1.7几下降到0.056左右，召回率和精确率已经平均调和F1都比较高。总的来说，baseline的检测效果是比较好的，我跑了两次，本地跑一次，修改参数后在服务器由跑了一次。

最好的模型的map达到83.10%,以下是一些检测指标的展示，这个是在服务器上面跑的baseline。

| 指标     | map    | f1     | recall | precision |
| -------- | ------ | ------ | ------ | --------- |
| 检测结果 | 83.10% | 79.14% | 74.47% | 84.88%    |

下面是每个类的map条形图展示。

<img src="D:\shuqikaohe\yolov5-pytorch-main\saved_model\map_out_baseline_silu\results\mAP.png" style="zoom:80%;" />

<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220729114610781.png" alt="image-20220729114610781" style="zoom:67%;" />

<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220729114948401.png" alt="image-20220729114948401" style="zoom:50%;" />





### change_hardswish

hardswish激活函数是一个分段函数，在尽可能的模拟silu的效果的同时降低计算程度，我就把silu改成x * F.hardsigmoid，理论上所得出的效果应该差不多，我还导入之前训练的30个epoch来训练的，训练时间确实短了不少，而且map也相对提升了一点点，精确率很高，但是其他召回率和平均调和F1相对低。检测的效果并没有baseline的效果好，我觉得是他的分段线性不能够像silu给网络带去一些非线性影响因素，网络相比于silu训出来的的简单。

此次训练得到的最好的模型map83.80%，指标展示如下。

| 指标     | map    | F1     | recall | precision |
| -------- | ------ | ------ | ------ | --------- |
| 检测结果 | 83.80% | 53.82% | 39.16% | 97.42%    |

下面是每个类的map的条形图展示

![](D:\shuqikaohe\yolov5-pytorch-main\saved_model\map_out_server_Hsilu\results\mAP.png)



<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220729115438983.png" alt="image-20220729115438983" style="zoom:67%;" />

<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220729115810590.png" alt="image-20220729115810590" style="zoom:50%;" />





### change_frelu

因为激活函数的非线性对网络，看到了一篇paper https://arxiv.org/pdf/2007.11824.pdf  介绍frelu能使网络性能和鲁棒性有很大的提升，还给出了在coco和imagenet上frelu检测效果相对于swish prelu relu 这三个函数好很多，它扩展了ReLU和PReLU到一个2D视觉激活，只增加了可忽略的计算开销，简单但有效，正好符合我的需求，于是我从官网中把这个自定义的frelu换到我的网络中进行训练，由于之前改的那个激活函数的检测效果不是很好，以为改了之后应该和silu效果差不多，没想到实际检测出来召回率和平均调和F1比silu的低很多，这是让我没有想到的，果然，这个非线性的卷积激活函数消除了激活函数中空间的不敏感，也真的取得了很好的效果，而且他的参数是可以学习并保留下来的。美中稍稍差以，他的召回率没有baseline的高，有些极少图像baseline检测的出来，他检测不出来，也算是差强人意。

| 指标     | map    | F1     | recall | precision |
| -------- | ------ | ------ | ------ | --------- |
| 检测效果 | 88.06% | 81.13% | 71.93% | 94.11%    |

以下是他的每个类的map展示

![](D:\shuqikaohe\yolov5-pytorch-main\saved_model\map_out_server2frelu\results\mAP.png)



检测效果图

<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220726133509813.png" alt="image-20220726133509813" style="zoom: 67%;" />

<img src="C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220729113959756.png" alt="image-20220729113959756" style="zoom: 50%;" />





## 总结

今天激活函数告一段落，基于我自己的理解以及我的实践，可能很多人认为改个激活函数很容易，但是想改一个正面的激活函数还是很难得，激活函数看似简单但是他对网络的影响是非常显著的，激活函数的求导、线性非线性、含不含参都是需要思考能不能有助于网络性能的提升。就激活函数，我花了很长时间去调整，光训练我就跑了四次，每一个得到的结果不经相同，根据消融实验不同指标，让我对不同激活函数同一网络有了进一步的理解。

