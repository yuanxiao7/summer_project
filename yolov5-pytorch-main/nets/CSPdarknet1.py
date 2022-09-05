import torch
import torch.nn as nn
from utils.activations import FReLU, Hardswish
from utils.attentions import se_block

class SiLU(nn.Module):
    @staticmethod
    def forward(x):
        return x * torch.sigmoid(x)


# 自定义自动padding模块
def autopad(k, p=None):
    if p is None:
        p = k // 2 if isinstance(k, int) else [x // 2 for x in k]
        # auto-pad #如果k是整数，p为k与2整除后向下取整；如果k是列表等，p对应的是列表中每个元素整除2。
    return p


# 3层 ：标准卷积 + bn + act
class CBA(nn.Module):
    def __init__(self, c1, c2, k=1, s=1, p=None, g=1, act=True):  # ch_in=3, ch_out=64, kernel=3, stride, padding, groups  k=3
        super(CBA, self).__init__()
        self.conv1 = Conv(c1, c1*2, k, 2, 1, g, act)  # act激活函数
        self.conv2 = Conv(c1*2, c2, 1, s, p, g, act)  # act激活函数

    def forward(self, x):  # 注意，这里的x的维度是4维的即  [b, c, h, w]up主解释时说的是一张图片即b=1
        # 320, 320, 12 => 320, 320, 64
        return self.conv2(self.conv1(x))



# 标准卷积 + bn + act
class Conv(nn.Module):
    def __init__(self, c1, c2, k=1, s=1, p=None, g=1, act=True):
        super(Conv, self).__init__()
        self.conv = nn.Conv2d(c1, c2, k, s, autopad(k, p), groups=g, bias=False)  # p 通过 autopad函数 自适应，保持shape对应
        self.bn = nn.BatchNorm2d(c2, eps=0.001, momentum=0.03)
        # self.act    = SiLU() if act is True else (act if isinstance(act, nn.Module) else nn.Identity())  # 加入非线性因素
        self.act = FReLU(c2) if act is True else (act if isinstance(act, nn.Module) else nn.Identity())
        # self.act    = Hardswish() if act is True else (act if isinstance(act, nn.Module) else nn.Identity())
        # 加入非线性因素  frelu目前除了召回率其他都比baseline好的模型

    def forward(self, x):
        return self.act(self.bn(self.conv(x)))  # 完整的经过一层卷积操作 即，conv + bn + act



class SE_Conv(nn.Module):
    # CSP Bottleneck with 3 convolutions
    def __init__(self, c1, c2):  # ch_in, ch_out, number, shortcut, groups, expansion
        super(SE_Conv, self).__init__()
        self.cv1 = Conv(c1, c1, 1, 1)
        self.cv2 = Conv(2 * c1, c2, 1)  # act=FReLU(c2)
        self.se_block = se_block(c2)

    def forward(self, x):
        return self.cv2(torch.cat(  # 两次调整的cat
            (
                self.cv1(x),
                self.se_block(x)
            )
            , dim=1))



# 深度可分离卷积
class depth_conv(nn.Module):
    def __init__(self, ch_in, ch_out,k=1, s=1, p=None, act=True):
        super(depth_conv, self).__init__()
        self.dep_conv = nn.Conv2d(ch_in, ch_in, k, s, autopad(k, p), groups=ch_in, bias=False)
        self.poi_conv = nn.Conv2d(ch_in, ch_out, kernel_size=1)
        self.act = FReLU(ch_out) if act is True else (act if isinstance(act, nn.Module) else nn.Identity())

    def forward(self, x):
        x = self.dep_conv(x)
        x = self.poi_conv(x)
        x = self.act(x)
        return x

# block循环内部
class Bottleneck(nn.Module):
    # Standard bottleneck
    def __init__(self, c1, c2, shortcut=True, g=1, e=0.5):  # ch_in, ch_out, shortcut, groups, expansion
        super(Bottleneck, self).__init__()
        c_ = int(c2 * e)  # hidden channels
        self.cv1 = depth_conv(c1, c_, 1, 1)
        self.cv2 = depth_conv(c_, c2, 3, 1)
        self.add = shortcut and c1 == c2

    def forward(self, x):
        return x + self.cv2(self. cv1(x)) if self.add else self.cv2(self.cv1(x))  # 判断输入和输出通道数是否相同，相同就cat
    # 先进行卷积一再进行卷积二，若x与卷积二输出同且shortcut为ture就返回x+conv12的cat，否则就只返回输出

# block
class C3(nn.Module):
    # CSP Bottleneck with 3 convolutions
    def __init__(self, c1, c2, n=1, shortcut=True, g=1, e=0.5):  # ch_in, ch_out, number, shortcut, groups, expansion
        super(C3, self).__init__()
        c_ = int(c2 * e)  # hidden channels
        self.cv1 = depth_conv(c1, c_, 1, 1)
        self.cv2 = depth_conv(c1, c_, 1, 1)
        self.cv3 = Conv(c_, c2, 1)  # act=FReLU(c2)
        self.m = nn.Sequential(*[Bottleneck(c_, c_, shortcut, g, e=1.0) for _ in range(n)])  # n即number 残差快的堆叠次数
        # self.m = nn.Sequential(*[CrossConv(c_, c_, 3, 1, g, 1.0, shortcut) for _ in range(n)])  *表示解释出列表里的网络结构

    def forward(self, x):
        return self.cv3(self.m(self.cv1(x)) + self.cv2(x))   # add 两部分整合到一起，标准卷积好一些


# 卷积加pooling
class SPP(nn.Module):
    # Spatial pyramid pooling layer used in YOLOv3-SPP
    def __init__(self, c1, c2, k=(5, 9, 13)):
        super(SPP, self).__init__()
        c_ = c1 // 2  # hidden channels
        self.cv1 = depth_conv(c1, c_, 1, 1)
        self.cv2 = Conv(c_ * (len(k) + 1), c2, 1, 1)
        self.m = nn.ModuleList([nn.MaxPool2d(kernel_size=x, stride=1, padding=x // 2) for x in k])
        # self.m为三层不同的kernel形成的最大池化net列表，输出维度=输入维度  //先做除法，再做向下取整

    def forward(self, x):
        x = self.cv1(x)
        return self.cv2(torch.cat([x] + [m(x) for m in self.m], 1))   # cat 两部分整合到一起，标准卷积好一些
        # 三个输出与x cat ch_out变为4倍的x的ch_in 即， c_ * (len(k) + 1)


class CSPDarknet(nn.Module):
    def __init__(self, base_channels, base_depth, phi, pretrained):
        super().__init__()
        # -----------------------------------------------#
        #   输入图片是640, 640, 3    初始 base_depth=3
        #   初始的基本通道base_channels是64
        # -----------------------------------------------#

        # -----------------------------------------------#
        #   利用focus网络结构进行特征提取
        #   640, 640, 3 -> 320, 320, 12 -> 320, 320, 64
        # -----------------------------------------------#
        self.stem = nn.Sequential(
            CBA(3, base_channels, k=3),
            Conv(base_channels, base_channels, 3, 1),
            SE_Conv(base_channels, base_channels)  # 加上通道注意力
            # depth_conv(base_channels, base_channels, 3, 1)  # 最开始改网络结构的组件
        )

        # -----------------------------------------------#
        #   完成卷积之后，320, 320, 64 -> 160, 160, 128   (320 +2p)/2 + 1 = 160
        #   完成CSPlayer之后，160, 160, 128 -> 160, 160, 128
        # -----------------------------------------------#
        self.dark2 = nn.Sequential(
            # 320, 320, 64 -> 160, 160, 128
            depth_conv(base_channels, base_channels * 2, 3, 2),
            # 160, 160, 128 -> 160, 160, 128
            C3(base_channels * 2, base_channels * 2, base_depth),
        )

        # -----------------------------------------------#
        #   完成卷积之后，160, 160, 128 -> 80, 80, 256
        #   完成CSPlayer之后，80, 80, 256 -> 80, 80, 256
        #                   在这里引出有效特征层80, 80, 256
        #                   进行加强特征提取网络FPN的构建  FPN金字塔
        # -----------------------------------------------#
        self.dark3 = nn.Sequential(
            depth_conv(base_channels * 2, base_channels * 4, 3, 2),
            C3(base_channels * 4, base_channels * 4, base_depth * 2),
        )

        # -----------------------------------------------#
        #   完成卷积之后，80, 80, 256 -> 40, 40, 512
        #   完成CSPlayer之后，40, 40, 512 -> 40, 40, 512
        #                   在这里引出有效特征层40, 40, 512
        #                   进行加强特征提取网络FPN的构建
        # -----------------------------------------------#
        self.dark4 = nn.Sequential(
            depth_conv(base_channels * 4, base_channels * 8, 3, 2),
            C3(base_channels * 8, base_channels * 8, base_depth * 2),
        )

        # -----------------------------------------------#
        #   完成卷积之后，40, 40, 512 -> 20, 20, 1024
        #   完成SPP之后，20, 20, 1024 -> 20, 20, 1024
        #   完成CSPlayer之后，20, 20, 1024 -> 20, 20, 1024
        # -----------------------------------------------#
        self.dark5 = nn.Sequential(
            depth_conv(base_channels * 8, base_channels * 16, 3, 2),
            SPP(base_channels * 16, base_channels * 16),
            C3(base_channels * 16, base_channels * 16, base_depth, shortcut=False),
        )
        # 冻结训练，直接用up主那里的网络权值练
        if pretrained:
            url = {
                's': 'https://github.com/bubbliiiing/yolov5-pytorch/releases/download/v1.0/cspdarknet_s_backbone.pth',
                'm': 'https://github.com/bubbliiiing/yolov5-pytorch/releases/download/v1.0/cspdarknet_m_backbone.pth',
                'l': 'https://github.com/bubbliiiing/yolov5-pytorch/releases/download/v1.0/cspdarknet_l_backbone.pth',
                'x': 'https://github.com/bubbliiiing/yolov5-pytorch/releases/download/v1.0/cspdarknet_x_backbone.pth',
            }[phi]
            checkpoint = torch.hub.load_state_dict_from_url(url=url, map_location="cpu", model_dir="./model_data")
            self.load_state_dict(checkpoint, strict=False)
            print("Load weights from ", url.split('/')[-1])

    def forward(self, x):
        x = self.stem(x)
        x = self.dark2(x)
        # -----------------------------------------------#
        #   dark3的输出为80, 80, 256，是一个有效特征层
        # -----------------------------------------------#
        x = self.dark3(x)
        feat1 = x
        # -----------------------------------------------#
        #   dark4的输出为40, 40, 512，是一个有效特征层
        # -----------------------------------------------#
        x = self.dark4(x)
        feat2 = x
        # -----------------------------------------------#
        #   dark5的输出为20, 20, 1024，是一个有效特征层
        # -----------------------------------------------#
        x = self.dark5(x)
        feat3 = x
        return feat1, feat2, feat3

# 实例化CSP网络，查看变量参数
# device = torch.device("cuda")
# net = CSPDarknet(64, 1, 3, False).to(device)
# print(net)
# # summary(net, (3, 640, 640))
# a = torch.randn(1, 3, 640, 640).to(device)
#
# if __name__=="__main__":
#     b1, b2, b3 = net.forward(a)
#     print(b1.shape)
#     print(b2.shape)
#     print(b3.shape)
# detection result：
# torch.Size([1, 64, 320, 320])  X
# torch.Size([1, 256, 80, 80])
# torch.Size([1, 512, 40, 40])
# torch.Size([1, 1024, 20, 20])
