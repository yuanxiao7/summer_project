import torch
import numpy as np
import torch.nn as nn
import os
from multiprocessing import Process
import cv2

# %matplotlib inline
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np





content = torch.load('weights/best_epoch_weights.pth')
print(content.keys())

# def sigmoid(x):
#     return 1/(1+np.exp(-x))
#
# x = np.linspace(-10,10)
# ##### 绘制sigmoid图像
# fig = plt.figure()
# y_sigmoid = 1/(1+np.exp(-x))
# ax = fig.add_subplot(321)
# ax.plot(x,y_sigmoid,color='blue')
# ax.grid()
# ax.set_title('(a) Sigmoid')
# ax.spines['right'].set_color('none') # 去除右边界线
# ax.spines['top'].set_color('none') # 去除上边界线
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))
#
# ##### 绘制Tanh图像
# ax = fig.add_subplot(322)
# y_tanh = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
# ax.plot(x,y_tanh,color='blue')
# ax.grid()
# ax.set_title('(b) Tanh')
# ax.spines['right'].set_color('none') # 去除右边界线
# ax.spines['top'].set_color('none') # 去除上边界线
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))
#
# ##### 绘制Relu图像
# ax = fig.add_subplot(323)
# y_relu = np.array([0*item  if item<0 else item for item in x ])
# ax.plot(x,y_relu,color='darkviolet')
# ax.grid()
# ax.set_title('(c) ReLu')
# ax.spines['right'].set_color('none') # 去除右边界线
# ax.spines['top'].set_color('none') # 去除上边界线
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))
#
# ##### 绘制Leaky Relu图像
# ax = fig.add_subplot(324)
# y_relu = np.array([0.2*item  if item<0 else item for item in x ])
# ax.plot(x,y_relu,color='darkviolet')
# ax.grid()
# ax.set_title('(d) Leaky Relu')
# ax.spines['right'].set_color('none') # 去除右边界线
# ax.spines['top'].set_color('none') # 去除上边界线
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))
#
# ##### 绘制ELU图像
# ax = fig.add_subplot(325)
# y_elu = np.array([2.0*(np.exp(item)-1)  if item<0 else item for item in x ])
# ax.plot(x,y_elu,color='darkviolet')
# ax.grid()
# ax.set_title('(d) ELU alpha=2.0')
# ax.spines['right'].set_color('none') # 去除右边界线
# ax.spines['top'].set_color('none') # 去除上边界线
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))
#
#
# class SiLU(nn.Module):
#     @staticmethod
#     def forward(x):
#         return x * torch.sigmoid(x)


# ax = fig.add_subplot(326)
# y_sigmoid_dev = x * sigmoid(x)
# ax.plot(x,y_sigmoid_dev,color='green')
# ax.grid()
# ax.set_title('(e) SiLU')
# ax.spines['right'].set_color('none') # 去除右边界线
# ax.spines['top'].set_color('none') # 去除上边界线
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))
#
# plt.tight_layout()
# plt.savefig('Activation.png')
# plt.show()


# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(10, 4))
# plt.scatter(2, 4)
# plt.show()
#


#
# # 元素树
# import xml.etree.ElementTree as ET
#
# tree = ET.parse('sample.xml')
# print(tree)
# root = tree.getroot()
# print(root)
# for obj in root.iter('object'):
#     print(obj)


# <xml.etree.ElementTree.ElementTree object at 0x0000022D01F3C730>
# <Element 'data' at 0x0000022D0B3119A0>
#

# # anchor的结果预测   去留判定
# a = torch.tensor([[0., 2., 1., 2.],
#                  [1., 2., 0., 1.],
#                  [0., 2., 1., 0.]])
# print(a)
# mark = [True, False, True]
# mark1 = [1., 0., 2.]
#
# print(a[:, -1])
# print(a[a[:, -1] == 1.])



# mark和unique用法
# a = torch.tensor([[0., 2., 1., 2.],
#                  [1., 2., 0., 1.],
#                  [0., 2., 1., 0.]])
# print(a)
# mark = [True, False, True]
# print(a.unique())  # 不重复取出所有的值，按升序排列
# print(a[mark])  # 去除对应维度的值

# tensor([[0., 2., 1., 2.],
#         [1., 2., 0., 1.],
#         [0., 2., 1., 0.]])
# tensor([0., 1., 2.])
# tensor([[0., 2., 1., 2.],
#         [0., 2., 1., 0.]])





# # yolov5先验框的形成
# anchors = [(3.625, 2.8125), (4.875, 6.1875), (11.65625, 10.1875)]
# a = torch.randn(1, 3, 20, 20, 80)
# # print(a)
# print(a.shape)
# print(a[..., 0].shape)
# a1 = torch.sigmoid(a[..., 0])
# # print(a1)
# # print(a1.shape)
# FloatTensor = torch.cuda.FloatTensor if a.is_cuda else torch.FloatTensor
# LongTensor = torch.cuda.LongTensor if a.is_cuda else torch.LongTensor
#
# anchor_w = FloatTensor(anchors).index_select(1, LongTensor([0]))
# anchor_h = FloatTensor(anchors).index_select(1, LongTensor([1]))
# print(anchor_h)
# anchor_w1 = anchor_w.repeat(1, 1)
# print(anchor_w1.shape)
# anchor_w2 = anchor_w.repeat(1, 1).repeat(1, 1, 20 * 20)
# print(anchor_w2.shape)
# anchor_w3 = anchor_w.repeat(1, 1).repeat(1, 1, 20 * 20).view(a1.shape)
# print(anchor_w3.shape)
# anchor_h = anchor_h.repeat(1, 1).repeat(1, 1, 20 * 20).view(a1.shape)

# torch.Size([1, 3, 20, 20, 80])
# torch.Size([1, 3, 20, 20])
# tensor([[ 2.8125],
#         [ 6.1875],
#         [10.1875]])
# torch.Size([3, 1])
# torch.Size([1, 3, 400])
# torch.Size([1, 3, 20, 20])




# 、、、、、focus特征提取原理实现，保留了特征![](C:/Users/Happy/AppData/Roaming/Tencent/QQ/Temp/)M14SEALAJW$TP)X%O~E)~P.png)
# a = torch.randn(1, 1, 4, 4)  # [b, c, h, w]不要看成[c, h, w],因为一般会批量处理

# print(a)
# print(a[..., ::2, ::2])  # 由第0行，第0列开始，横着隔一个，竖着隔一个取
# print(a[..., 1::2, ::2])  # 第1行，第0列开始，横着隔一个，竖着隔一个取
# print(a[..., ::2, 1::2])  # 第0行，第1列开始，横着隔一个，竖着隔一个取
# print(a[..., 1::2, 1::2])  # 第1行，第1列开始，横着隔一个，竖着隔一个取
# b = torch.cat([a[..., ::2, ::2],
#                a[..., 1::2, ::2],
#                a[..., ::2, 1::2],
#                a[..., 1::2, 1::2],
#                ], 1)
#
# print(a.shape)
# print(b.shape)
# print(b)
# image_shape = np.array(np.shape(a)[0:2])
# print(np.shape(a))
# print(np.shape(a)[0:2])
# print(np.array(np.shape(a)[0:2]))
# print(a)
# print(image_shape)
#


# 、、、、、试验，控制可视图片的大小的调整
# from PIL import Image
#
# im = Image.open(r"E:\DL_environments\torch\bubbliiiing\yolov5-pytorch-main\img\1-1.png")
# width, height = im.size
# print(np.shape(im))
#
# left = 1
# top = height / 110  # 分母越大，图片高度越高
# right = 1700
# bottom = 3 * height / 3  # 分母越小，图片低处越低
# im1 = im.crop((left, top, right, bottom))
# newsize = (2000, 1000)
# im1 = im1.resize(newsize)
# im1.show()


# 、、、、、不失真的resize 灰图pading
# from PIL import Image
#
#
# def letterbox_image(image, size):
#     # 对图片进行resize，使图片不失真。在空缺的地方进行padding
#     iw, ih = image.size  # 宽大于高
#     w, h = size
#     scale = min(w / iw, h / ih)
#     print(scale)
#     print(iw*scale)
#     print(ih*scale)
#     nw = int(iw * scale)
#     nh = int(ih * scale)
#
#     image = image.resize((nw, nh), Image.BICUBIC)  # Image.BICUBIC：图像插值-双三次插值  可认为在原图像后加灰色图，根据指定维度phi
#     new_image = Image.new('RGB', size, (128, 128, 128))
#     new_image.paste(image, ((w - nw) // 2, (h - nh) // 2))
#     return new_image
#
#、、、、、
# img = Image.open(r"img\1-1.jpg")
# new_image = letterbox_image(img, [640, 640])
# new_image.show()
#

# from PIL import Image
# import matplotlib.pyplot as plt
#
# img = Image.new("RGB",(500,500),(128,128,128)) # 128为灰度图
# img.show()


# 、、、、matplotlib画图在pycharm中要show才看得见
# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(0, 35)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()
































