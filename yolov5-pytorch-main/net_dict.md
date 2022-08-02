## 网络结构



### print(YloBody)  

直接打印网络结构，一目了然！

```python
YoloBody(
  (backbone): CSPDarknet(
    (stem): Focus(
      (conv): Conv(
        (conv): Conv2d(12, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): FReLU(
          (conv): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=32, bias=False)
          (bn): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
      )
    )
    (dark2): Sequential(
      (0): Conv(
        (conv): Conv2d(32, 64, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): FReLU(
          (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
          (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
      )
      (1): C3(
        (cv1): Conv(
          (conv): Conv2d(64, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=32, bias=False)
            (bn): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(64, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=32, bias=False)
            (bn): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv3): Conv(
          (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
            (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (m): Sequential(
          (0): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(32, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=32, bias=False)
                (bn): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(32, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=32, bias=False)
                (bn): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
        )
      )
    )
    (dark3): Sequential(
      (0): Conv(
        (conv): Conv2d(64, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): FReLU(
          (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
          (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
      )
      (1): C3(
        (cv1): Conv(
          (conv): Conv2d(128, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
            (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(128, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
            (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv3): Conv(
          (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
            (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (m): Sequential(
          (0): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
          (1): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
          (2): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
        )
      )
    )
    (dark4): Sequential(
      (0): Conv(
        (conv): Conv2d(128, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): FReLU(
          (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
          (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
      )
      (1): C3(
        (cv1): Conv(
          (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
            (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
            (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv3): Conv(
          (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
            (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (m): Sequential(
          (0): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
                (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
                (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
          (1): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
                (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
                (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
          (2): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
                (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
                (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
        )
      )
    )
    (dark5): Sequential(
      (0): Conv(
        (conv): Conv2d(256, 512, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
        (act): FReLU(
          (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=512, bias=False)
          (bn): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
      )
      (1): SPP(
        (cv1): Conv(
          (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
            (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(1024, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=512, bias=False)
            (bn): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (m): ModuleList(
          (0): MaxPool2d(kernel_size=5, stride=1, padding=2, dilation=1, ceil_mode=False)
          (1): MaxPool2d(kernel_size=9, stride=1, padding=4, dilation=1, ceil_mode=False)
          (2): MaxPool2d(kernel_size=13, stride=1, padding=6, dilation=1, ceil_mode=False)
        )
      )
      (2): C3(
        (cv1): Conv(
          (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
            (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
            (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv3): Conv(
          (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=512, bias=False)
            (bn): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (m): Sequential(
          (0): Bottleneck(
            (cv1): Conv(
              (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
              (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
                (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
            (cv2): Conv(
              (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
              (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
              (act): FReLU(
                (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
                (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
              )
            )
          )
        )
      )
    )
  )
  (upsample): Upsample(scale_factor=2.0, mode=nearest)
  (conv_for_feat3): Conv(
    (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
    (act): FReLU(
      (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
      (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (conv3_for_upsample1): C3(
    (cv1): Conv(
      (conv): Conv2d(512, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
        (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv2): Conv(
      (conv): Conv2d(512, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
        (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv3): Conv(
      (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
        (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (m): Sequential(
      (0): Bottleneck(
        (cv1): Conv(
          (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
            (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
          (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
            (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
      )
    )
  )
  (conv_for_feat2): Conv(
    (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
    (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
    (act): FReLU(
      (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
      (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (conv3_for_upsample2): C3(
    (cv1): Conv(
      (conv): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
        (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv2): Conv(
      (conv): Conv2d(256, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
        (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv3): Conv(
      (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
        (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (m): Sequential(
      (0): Bottleneck(
        (cv1): Conv(
          (conv): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
            (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
          (bn): BatchNorm2d(64, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
            (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
      )
    )
  )
  (down_sample1): Conv(
    (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
    (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
    (act): FReLU(
      (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
      (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (conv3_for_downsample1): C3(
    (cv1): Conv(
      (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
        (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv2): Conv(
      (conv): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
        (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv3): Conv(
      (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
        (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (m): Sequential(
      (0): Bottleneck(
        (cv1): Conv(
          (conv): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
            (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
          (bn): BatchNorm2d(128, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
            (bn): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
      )
    )
  )
  (down_sample2): Conv(
    (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
    (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
    (act): FReLU(
      (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
      (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (conv3_for_downsample2): C3(
    (cv1): Conv(
      (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
        (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv2): Conv(
      (conv): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
        (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (cv3): Conv(
      (conv): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
      (bn): BatchNorm2d(512, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
      (act): FReLU(
        (conv): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=512, bias=False)
        (bn): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (m): Sequential(
      (0): Bottleneck(
        (cv1): Conv(
          (conv): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
            (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
        (cv2): Conv(
          (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
          (bn): BatchNorm2d(256, eps=0.001, momentum=0.03, affine=True, track_running_stats=True)
          (act): FReLU(
            (conv): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=256, bias=False)
            (bn): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          )
        )
      )
    )
  )
  (yolo_head_P3): Conv2d(128, 75, kernel_size=(1, 1), stride=(1, 1))
  (yolo_head_P4): Conv2d(256, 75, kernel_size=(1, 1), stride=(1, 1))
  (yolo_head_P5): Conv2d(512, 75, kernel_size=(1, 1), stride=(1, 1))
)
```





### summary.py  

- 打印网络结构脚本

表格如下

这里得pai指定的是 ‘s’ 最小的那个模型，可以看到，我在yolo neck得进口处添加了了注意力机制

```python
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1         [-1, 32, 320, 320]           3,456
       BatchNorm2d-2         [-1, 32, 320, 320]              64
              SiLU-3         [-1, 32, 320, 320]               0
              Conv-4         [-1, 32, 320, 320]               0
             Focus-5         [-1, 32, 320, 320]               0
            Conv2d-6         [-1, 64, 160, 160]          18,432
       BatchNorm2d-7         [-1, 64, 160, 160]             128
              SiLU-8         [-1, 64, 160, 160]               0
              Conv-9         [-1, 64, 160, 160]               0
           Conv2d-10         [-1, 32, 160, 160]           2,048
      BatchNorm2d-11         [-1, 32, 160, 160]              64
             SiLU-12         [-1, 32, 160, 160]               0
             Conv-13         [-1, 32, 160, 160]               0
           Conv2d-14         [-1, 32, 160, 160]           1,024
      BatchNorm2d-15         [-1, 32, 160, 160]              64
             SiLU-16         [-1, 32, 160, 160]               0
             Conv-17         [-1, 32, 160, 160]               0
           Conv2d-18         [-1, 32, 160, 160]           9,216
      BatchNorm2d-19         [-1, 32, 160, 160]              64
             SiLU-20         [-1, 32, 160, 160]               0
             Conv-21         [-1, 32, 160, 160]               0
       Bottleneck-22         [-1, 32, 160, 160]               0
           Conv2d-23         [-1, 32, 160, 160]           2,048
      BatchNorm2d-24         [-1, 32, 160, 160]              64
             SiLU-25         [-1, 32, 160, 160]               0
             Conv-26         [-1, 32, 160, 160]               0
           Conv2d-27         [-1, 64, 160, 160]           4,096
      BatchNorm2d-28         [-1, 64, 160, 160]             128
             SiLU-29         [-1, 64, 160, 160]               0
             Conv-30         [-1, 64, 160, 160]               0
               C3-31         [-1, 64, 160, 160]               0
           Conv2d-32          [-1, 128, 80, 80]          73,728
      BatchNorm2d-33          [-1, 128, 80, 80]             256
             SiLU-34          [-1, 128, 80, 80]               0
             Conv-35          [-1, 128, 80, 80]               0
           Conv2d-36           [-1, 64, 80, 80]           8,192
      BatchNorm2d-37           [-1, 64, 80, 80]             128
             SiLU-38           [-1, 64, 80, 80]               0
             Conv-39           [-1, 64, 80, 80]               0
           Conv2d-40           [-1, 64, 80, 80]           4,096
      BatchNorm2d-41           [-1, 64, 80, 80]             128
             SiLU-42           [-1, 64, 80, 80]               0
             Conv-43           [-1, 64, 80, 80]               0
           Conv2d-44           [-1, 64, 80, 80]          36,864
      BatchNorm2d-45           [-1, 64, 80, 80]             128
             SiLU-46           [-1, 64, 80, 80]               0
             Conv-47           [-1, 64, 80, 80]               0
       Bottleneck-48           [-1, 64, 80, 80]               0
           Conv2d-49           [-1, 64, 80, 80]           4,096
      BatchNorm2d-50           [-1, 64, 80, 80]             128
             SiLU-51           [-1, 64, 80, 80]               0
             Conv-52           [-1, 64, 80, 80]               0
           Conv2d-53           [-1, 64, 80, 80]          36,864
      BatchNorm2d-54           [-1, 64, 80, 80]             128
             SiLU-55           [-1, 64, 80, 80]               0
             Conv-56           [-1, 64, 80, 80]               0
       Bottleneck-57           [-1, 64, 80, 80]               0
           Conv2d-58           [-1, 64, 80, 80]           4,096
      BatchNorm2d-59           [-1, 64, 80, 80]             128
             SiLU-60           [-1, 64, 80, 80]               0
             Conv-61           [-1, 64, 80, 80]               0
           Conv2d-62           [-1, 64, 80, 80]          36,864
      BatchNorm2d-63           [-1, 64, 80, 80]             128
             SiLU-64           [-1, 64, 80, 80]               0
             Conv-65           [-1, 64, 80, 80]               0
       Bottleneck-66           [-1, 64, 80, 80]               0
           Conv2d-67           [-1, 64, 80, 80]           8,192
      BatchNorm2d-68           [-1, 64, 80, 80]             128
             SiLU-69           [-1, 64, 80, 80]               0
             Conv-70           [-1, 64, 80, 80]               0
           Conv2d-71          [-1, 128, 80, 80]          16,384
      BatchNorm2d-72          [-1, 128, 80, 80]             256
             SiLU-73          [-1, 128, 80, 80]               0
             Conv-74          [-1, 128, 80, 80]               0
               C3-75          [-1, 128, 80, 80]               0
           Conv2d-76          [-1, 256, 40, 40]         294,912
      BatchNorm2d-77          [-1, 256, 40, 40]             512
             SiLU-78          [-1, 256, 40, 40]               0
             Conv-79          [-1, 256, 40, 40]               0
           Conv2d-80          [-1, 128, 40, 40]          32,768
      BatchNorm2d-81          [-1, 128, 40, 40]             256
             SiLU-82          [-1, 128, 40, 40]               0
             Conv-83          [-1, 128, 40, 40]               0
           Conv2d-84          [-1, 128, 40, 40]          16,384
      BatchNorm2d-85          [-1, 128, 40, 40]             256
             SiLU-86          [-1, 128, 40, 40]               0
             Conv-87          [-1, 128, 40, 40]               0
           Conv2d-88          [-1, 128, 40, 40]         147,456
      BatchNorm2d-89          [-1, 128, 40, 40]             256
             SiLU-90          [-1, 128, 40, 40]               0
             Conv-91          [-1, 128, 40, 40]               0
       Bottleneck-92          [-1, 128, 40, 40]               0
           Conv2d-93          [-1, 128, 40, 40]          16,384
      BatchNorm2d-94          [-1, 128, 40, 40]             256
             SiLU-95          [-1, 128, 40, 40]               0
             Conv-96          [-1, 128, 40, 40]               0
           Conv2d-97          [-1, 128, 40, 40]         147,456
      BatchNorm2d-98          [-1, 128, 40, 40]             256
             SiLU-99          [-1, 128, 40, 40]               0
            Conv-100          [-1, 128, 40, 40]               0
      Bottleneck-101          [-1, 128, 40, 40]               0
          Conv2d-102          [-1, 128, 40, 40]          16,384
     BatchNorm2d-103          [-1, 128, 40, 40]             256
            SiLU-104          [-1, 128, 40, 40]               0
            Conv-105          [-1, 128, 40, 40]               0
          Conv2d-106          [-1, 128, 40, 40]         147,456
     BatchNorm2d-107          [-1, 128, 40, 40]             256
            SiLU-108          [-1, 128, 40, 40]               0
            Conv-109          [-1, 128, 40, 40]               0
      Bottleneck-110          [-1, 128, 40, 40]               0
          Conv2d-111          [-1, 128, 40, 40]          32,768
     BatchNorm2d-112          [-1, 128, 40, 40]             256
            SiLU-113          [-1, 128, 40, 40]               0
            Conv-114          [-1, 128, 40, 40]               0
          Conv2d-115          [-1, 256, 40, 40]          65,536
     BatchNorm2d-116          [-1, 256, 40, 40]             512
            SiLU-117          [-1, 256, 40, 40]               0
            Conv-118          [-1, 256, 40, 40]               0
              C3-119          [-1, 256, 40, 40]               0
          Conv2d-120          [-1, 512, 20, 20]       1,179,648
     BatchNorm2d-121          [-1, 512, 20, 20]           1,024
            SiLU-122          [-1, 512, 20, 20]               0
            Conv-123          [-1, 512, 20, 20]               0
          Conv2d-124          [-1, 256, 20, 20]         131,072
     BatchNorm2d-125          [-1, 256, 20, 20]             512
            SiLU-126          [-1, 256, 20, 20]               0
            Conv-127          [-1, 256, 20, 20]               0
       MaxPool2d-128          [-1, 256, 20, 20]               0
       MaxPool2d-129          [-1, 256, 20, 20]               0
       MaxPool2d-130          [-1, 256, 20, 20]               0
          Conv2d-131          [-1, 512, 20, 20]         524,288
     BatchNorm2d-132          [-1, 512, 20, 20]           1,024
            SiLU-133          [-1, 512, 20, 20]               0
            Conv-134          [-1, 512, 20, 20]               0
             SPP-135          [-1, 512, 20, 20]               0
          Conv2d-136          [-1, 256, 20, 20]         131,072
     BatchNorm2d-137          [-1, 256, 20, 20]             512
            SiLU-138          [-1, 256, 20, 20]               0
            Conv-139          [-1, 256, 20, 20]               0
          Conv2d-140          [-1, 256, 20, 20]          65,536
     BatchNorm2d-141          [-1, 256, 20, 20]             512
            SiLU-142          [-1, 256, 20, 20]               0
            Conv-143          [-1, 256, 20, 20]               0
          Conv2d-144          [-1, 256, 20, 20]         589,824
     BatchNorm2d-145          [-1, 256, 20, 20]             512
            SiLU-146          [-1, 256, 20, 20]               0
            Conv-147          [-1, 256, 20, 20]               0
      Bottleneck-148          [-1, 256, 20, 20]               0
          Conv2d-149          [-1, 256, 20, 20]         131,072
     BatchNorm2d-150          [-1, 256, 20, 20]             512
            SiLU-151          [-1, 256, 20, 20]               0
            Conv-152          [-1, 256, 20, 20]               0
          Conv2d-153          [-1, 512, 20, 20]         262,144
     BatchNorm2d-154          [-1, 512, 20, 20]           1,024
            SiLU-155          [-1, 512, 20, 20]               0
            Conv-156          [-1, 512, 20, 20]               0
              C3-157          [-1, 512, 20, 20]               0
      CSPDarknet-158  [[-1, 128, 80, 80], [-1, 256, 40, 40], [-1, 512, 20, 20]]               0
AdaptiveAvgPool2d-159            [-1, 128, 1, 1]               0
          Linear-160                    [-1, 8]           1,024
            ReLU-161                    [-1, 8]               0
          Linear-162                  [-1, 128]           1,024
         Sigmoid-163                  [-1, 128]               0
        se_block-164          [-1, 128, 80, 80]               0
AdaptiveAvgPool2d-165            [-1, 256, 1, 1]               0
          Linear-166                   [-1, 16]           4,096
            ReLU-167                   [-1, 16]               0
          Linear-168                  [-1, 256]           4,096
         Sigmoid-169                  [-1, 256]               0
        se_block-170          [-1, 256, 40, 40]               0
AdaptiveAvgPool2d-171            [-1, 512, 1, 1]               0
          Linear-172                   [-1, 32]          16,384
            ReLU-173                   [-1, 32]               0
          Linear-174                  [-1, 512]          16,384
         Sigmoid-175                  [-1, 512]               0
        se_block-176          [-1, 512, 20, 20]               0
          Conv2d-177          [-1, 256, 20, 20]         131,072
     BatchNorm2d-178          [-1, 256, 20, 20]             512
            SiLU-179          [-1, 256, 20, 20]               0
            Conv-180          [-1, 256, 20, 20]               0
        Upsample-181          [-1, 256, 40, 40]               0
          Conv2d-182          [-1, 128, 40, 40]          65,536
     BatchNorm2d-183          [-1, 128, 40, 40]             256
            SiLU-184          [-1, 128, 40, 40]               0
            Conv-185          [-1, 128, 40, 40]               0
          Conv2d-186          [-1, 128, 40, 40]          16,384
     BatchNorm2d-187          [-1, 128, 40, 40]             256
            SiLU-188          [-1, 128, 40, 40]               0
            Conv-189          [-1, 128, 40, 40]               0
          Conv2d-190          [-1, 128, 40, 40]         147,456
     BatchNorm2d-191          [-1, 128, 40, 40]             256
            SiLU-192          [-1, 128, 40, 40]               0
            Conv-193          [-1, 128, 40, 40]               0
      Bottleneck-194          [-1, 128, 40, 40]               0
          Conv2d-195          [-1, 128, 40, 40]          65,536
     BatchNorm2d-196          [-1, 128, 40, 40]             256
            SiLU-197          [-1, 128, 40, 40]               0
            Conv-198          [-1, 128, 40, 40]               0
          Conv2d-199          [-1, 256, 40, 40]          65,536
     BatchNorm2d-200          [-1, 256, 40, 40]             512
            SiLU-201          [-1, 256, 40, 40]               0
            Conv-202          [-1, 256, 40, 40]               0
              C3-203          [-1, 256, 40, 40]               0
          Conv2d-204          [-1, 128, 40, 40]          32,768
     BatchNorm2d-205          [-1, 128, 40, 40]             256
            SiLU-206          [-1, 128, 40, 40]               0
            Conv-207          [-1, 128, 40, 40]               0
        Upsample-208          [-1, 128, 80, 80]               0
          Conv2d-209           [-1, 64, 80, 80]          16,384
     BatchNorm2d-210           [-1, 64, 80, 80]             128
            SiLU-211           [-1, 64, 80, 80]               0
            Conv-212           [-1, 64, 80, 80]               0
          Conv2d-213           [-1, 64, 80, 80]           4,096
     BatchNorm2d-214           [-1, 64, 80, 80]             128
            SiLU-215           [-1, 64, 80, 80]               0
            Conv-216           [-1, 64, 80, 80]               0
          Conv2d-217           [-1, 64, 80, 80]          36,864
     BatchNorm2d-218           [-1, 64, 80, 80]             128
            SiLU-219           [-1, 64, 80, 80]               0
            Conv-220           [-1, 64, 80, 80]               0
      Bottleneck-221           [-1, 64, 80, 80]               0
          Conv2d-222           [-1, 64, 80, 80]          16,384
     BatchNorm2d-223           [-1, 64, 80, 80]             128
            SiLU-224           [-1, 64, 80, 80]               0
            Conv-225           [-1, 64, 80, 80]               0
          Conv2d-226          [-1, 128, 80, 80]          16,384
     BatchNorm2d-227          [-1, 128, 80, 80]             256
            SiLU-228          [-1, 128, 80, 80]               0
            Conv-229          [-1, 128, 80, 80]               0
              C3-230          [-1, 128, 80, 80]               0
          Conv2d-231          [-1, 128, 40, 40]         147,456
     BatchNorm2d-232          [-1, 128, 40, 40]             256
            SiLU-233          [-1, 128, 40, 40]               0
            Conv-234          [-1, 128, 40, 40]               0
          Conv2d-235          [-1, 128, 40, 40]          32,768
     BatchNorm2d-236          [-1, 128, 40, 40]             256
            SiLU-237          [-1, 128, 40, 40]               0
            Conv-238          [-1, 128, 40, 40]               0
          Conv2d-239          [-1, 128, 40, 40]          16,384
     BatchNorm2d-240          [-1, 128, 40, 40]             256
            SiLU-241          [-1, 128, 40, 40]               0
            Conv-242          [-1, 128, 40, 40]               0
          Conv2d-243          [-1, 128, 40, 40]         147,456
     BatchNorm2d-244          [-1, 128, 40, 40]             256
            SiLU-245          [-1, 128, 40, 40]               0
            Conv-246          [-1, 128, 40, 40]               0
      Bottleneck-247          [-1, 128, 40, 40]               0
          Conv2d-248          [-1, 128, 40, 40]          32,768
     BatchNorm2d-249          [-1, 128, 40, 40]             256
            SiLU-250          [-1, 128, 40, 40]               0
            Conv-251          [-1, 128, 40, 40]               0
          Conv2d-252          [-1, 256, 40, 40]          65,536
     BatchNorm2d-253          [-1, 256, 40, 40]             512
            SiLU-254          [-1, 256, 40, 40]               0
            Conv-255          [-1, 256, 40, 40]               0
              C3-256          [-1, 256, 40, 40]               0
          Conv2d-257          [-1, 256, 20, 20]         589,824
     BatchNorm2d-258          [-1, 256, 20, 20]             512
            SiLU-259          [-1, 256, 20, 20]               0
            Conv-260          [-1, 256, 20, 20]               0
          Conv2d-261          [-1, 256, 20, 20]         131,072
     BatchNorm2d-262          [-1, 256, 20, 20]             512
            SiLU-263          [-1, 256, 20, 20]               0
            Conv-264          [-1, 256, 20, 20]               0
          Conv2d-265          [-1, 256, 20, 20]          65,536
     BatchNorm2d-266          [-1, 256, 20, 20]             512
            SiLU-267          [-1, 256, 20, 20]               0
            Conv-268          [-1, 256, 20, 20]               0
          Conv2d-269          [-1, 256, 20, 20]         589,824
     BatchNorm2d-270          [-1, 256, 20, 20]             512
            SiLU-271          [-1, 256, 20, 20]               0
            Conv-272          [-1, 256, 20, 20]               0
      Bottleneck-273          [-1, 256, 20, 20]               0
          Conv2d-274          [-1, 256, 20, 20]         131,072
     BatchNorm2d-275          [-1, 256, 20, 20]             512
            SiLU-276          [-1, 256, 20, 20]               0
            Conv-277          [-1, 256, 20, 20]               0
          Conv2d-278          [-1, 512, 20, 20]         262,144
     BatchNorm2d-279          [-1, 512, 20, 20]           1,024
            SiLU-280          [-1, 512, 20, 20]               0
            Conv-281          [-1, 512, 20, 20]               0
              C3-282          [-1, 512, 20, 20]               0
          Conv2d-283           [-1, 75, 80, 80]           9,675
          Conv2d-284           [-1, 75, 40, 40]          19,275
          Conv2d-285           [-1, 75, 20, 20]          38,475
================================================================
Total params: 7,157,793
Trainable params: 7,157,793
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 4.69
Forward/backward pass size (MB): 866.55
Params size (MB): 27.30
Estimated Total Size (MB): 898.54
----------------------------------------------------------------
Total GFLOPS: 16.643G
Total params: 7.158M

```

