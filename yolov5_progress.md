# Explain  the  progress and result of yolov5

- **注明：这是跟着b导学习的yolov5，源码来源于b导的github**  https://github.com/bubbliiiing/yolov5-pytorch

（7月4日）

首先，我们先总网络结构开始。

CSPdarknet 跟yolov3的darknet53网络架构有的很带的改动，不再是简单的残差堆叠，把一个大的残差块，分成四部分，每一部分有一个conv和再次conv后的block堆叠，中间的残差块比较深，两边的较浅，在感受野最大的特征图之前还增加了spp由三个不同的kennel形成的最大池化，相比yolov3，特征提取深度更深。最重要的是是它能够在增加深度的同时，能够保持广度，而且还减少了网络层数，也就意味着减少了参数，使得网络更加轻量化。

然后到yolo_body部分，yolo_body部分增加了csplayer和倒三角的操作，特区到的特征更加充分，同时也增加了网络的复杂度，检测的效果更好。

网络结构如下所示

![](.\picture\8.png)



（7月5日）

yolo解码 

**借鉴出处**  https://blog.csdn.net/weixin_45377629/article/details/124144913 

再利用darknet和yolobody后得到3个yolo_head的输出，不同尺度之下，每个网格点均有先验框，网络训练过程会对先验框的参数进行调整，进而得到预测框，从不同尺度下预测框还原到原图输入的图像上，同时包括该框内目标预测的结果情况（预测框的位置、类别概率、置信度分数）



