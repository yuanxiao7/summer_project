

## web端学习

### 图片上传web居中展示

#### 说明

- 这个demo实现了一个简单的前后端get的通信，前端部分，写好标题，thml作为总框架，嵌套CSS style确定位置大小信息等，引入jQuery库，然后用input装几个按钮，打开本地文件，上传，获取按钮并用js绑定按钮的触发事件，前端通过$.get 根据路由给ab赋值，，后端request.args.get接收后打印并返回yueyue给前端，前端再将其在控制台上打印console.log出来。

flask_try.py

```python
import json

import flask

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

# 定义总路由
@app.route('/')
def index():
    return render_template('index.html')

 @app.route('/hello')
 def hello():
     a = request.args.get('a')
     print(a)
     b = request.args.get('b')
	    print(b)
     return "yueyue"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



```



index.html

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mnist手写数字识别</title>
    <style>
        #box {text-align: center}
        #img1 {width: 500px; height: 500px}
    </style>
    <script src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js"></script>
</head>
<body>
<div id="box">
    <h1>Mnist 手写数字识别</h1>
    <img src="https://blog.keter.top/img/touxiang.png" id="img1">
    <div>
        <input type="file" name="file">
        <input type="button" value="上传">
    </div>
    <h2>识别结果：</h2>
    <button id="b1">点击</button>
</div>
<script>
    $('#b1').click(function (){
        $.get('/hello?a=1&b=2',function (data){
            console.log(data)
        })
    })

</script>
</body>
</html>
```



web展示如下

![image-20220828130100142](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220828130100142.png)





## 用到Ajax 前端向后端post

- 这一个利用ajax与前端向后端post的demo，在前端定义json类型的数据，利用$.post将数据通过路由post给后端，后端有路由设置post方法接收，并返回值给后端，提示成功传输数据了！



flask_try

```python
import json

import flask

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

# 定义总路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_test', methods=['POST'])
def post_test():
    # 获取json类型数据
    data = request.get_json()  # dict
    print(data)
    da = {"a": 1, "b": 2}
    da = json.dumps(da)
    return da

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


```



index.html

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mnist手写数字识别</title>
    <style>
        #box {text-align: center}
        #img1 {width: 300px; height: 300px}
    </style>
    <script src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js"></script>
</head>
<body>
<div id="box">
    <h1>Mnist 手写数字识别</h1>
    <img src="https://blog.keter.top/img/touxiang.png" id="img1">
    <div>
        <input type="file" name="file">
        <input type="button" value="上传">
    </div>
    <h2>识别结果：</h2>
    <button id="b1">点击</button>
</div>
<script>
    $("#b1").click(function () {
        var data = {"a": 1,"b": 2}
        $.ajax({
            type: "POST",
            url: "/post_test",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),
            dataType: "json",
            success: function (data) {
                console.log("发送成功")
            },
        });
    })
</script>
</body>
</html>
```



![image-20220828134915042](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220828134915042.png)





在该路径下更改源码

![image-20220828193226516](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220828193226516.png)





## 手写数字实例

该web的文件目录如下：

只用到：detector.py ，flask_try.py ， Mnist_detect.py  ，index.html 这四个文件

![image-20220829000132294](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220829000132294.png)

- 首先，先准备好一个手写数字的demo，如下方代码所示，两三分钟就可以训完，得到训练模型可以直接用于预测。



### detecor.py

```python
import torch
import torch.nn as nn
from torch.utils.data import dataloader
import torchvision
import torch.nn.functional as F
import torch.optim as optim

n_epochs = 3
batch_size_train = 64
batch_size_test = 1000
learning_rate = 0.01
momentum = 0.5
log_interval = 10
random_seed = 1
torch.manual_seed(random_seed)

train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('./data/', train=True, download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size_train, shuffle=True)
test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('./data/', train=False, download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size_test, shuffle=True)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x)


network = Net()
optimizer = optim.SGD(network.parameters(), lr=learning_rate,
                      momentum=momentum)

train_losses = []
train_counter = []
test_losses = []
test_counter = [i * len(train_loader.dataset) for i in range(n_epochs + 1)]


def train(epoch):
    network.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = network(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))
            train_losses.append(loss.item())
            train_counter.append(
                (batch_idx * 64) + ((epoch - 1) * len(train_loader.dataset)))
            torch.save(network.state_dict(), './model.pth')
            torch.save(optimizer.state_dict(), './optimizer.pth')


def _test():
    network.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = network(data)
            test_loss += F.nll_loss(output, target, size_average=False).item()
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).sum()
    test_loss /= len(test_loader.dataset)
    test_losses.append(test_loss)
    print('\nTest set: Avg. loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

# 训练权重时撤掉注释，生成的权重默认保存在根目录下
# for epoch in range(1, n_epochs + 1):
#     train(epoch)
#     _test()
```



下面这个py文件算是一个Mnist检测与后端的接口

### Mnist_detect.py

```python
import torch
from PIL import Image
from detector import Net
from torchvision.transforms import functional
import numpy as np


@torch.no_grad()
def detect(img_path, model_path='./model.pth'):
    # 读取图片
    img = Image.open(img_path)
    img = img.convert('L')
    img = img.resize((28, 28))
    img = functional.pil_to_tensor(img) / 255.
    img = img.unsqueeze(0)
    # 加载模型
    model = Net()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    result = model(img)[0]
    result = np.argmax(result.tolist())
    return result


if __name__ == '__main__':
    result = detect(img_path='D:\shuqikaohe\yolov5-pytorch-main\code1\data\picture/1.jpg')
    print(result)

```



下面这部分就是后端flask_try.py文件，接收前端推送的信息，对图片进行检测，并将检测结果返回给前端。

### flask_try.py

```python
from flask import render_template
from flask import request

from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask import Flask, request
from Mnist_detect import detect
import json

app = Flask(__name__)

app.config["UPLOADED_PHOTOS_DEST"] = 'uploads'

photo = UploadSet('photos', IMAGES)
configure_uploads(app, photo)
patch_request_class(app)


# 定义总路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_test', methods=['POST'])
def post_test():
    # 获取json类型数据
    data = request.get_json()  # dict
    print(data)
    da = {"a": 1, "b": 2}
    da = json.dumps(da)
    return da

@app.route('/detector', methods=['POST'])
def detector():
    filename = photo.save(request.files['file']) #保存图片
    file_url = photo.url(filename) # 获取url
    path = photo.path(filename) # 获取存储路径
    result = detect(path)
    data = {'file_url': file_url, "detect_result": str(result)} # 构造返回数据
    data = json.dumps(data) # 转换为字符串
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```



前端

这个是在后端flask_try同目录下一个文件夹（这里是templates）下的前端文件index.html，主语文件存放方式，index.html就是负责在web上的展示，通过按钮来触发事件，向后端发送post请求并接收后端传过来的图片和预测结果，在网页上展示出来。

```css
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>首页</title>
    <style>
        #img {
            width: 300px;
            height: 300px
        }

        #box {
            text-align: center;
        }

    </style>
    <script src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js"></script>
</head>
<body>
<div id="box">
    <h2>Mnist手写数字识别</h2>
    <!--初始化一个img标签-->
    <img id="img" src=" ">
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="button" value="上传" id="upFileBtn">
    </form>
    <!-- 显示识别结果 -->
<!--    <p id="p1">识别结果：<nobr id="d1"> <nobr/> </p>-->
    <p>识别结果：<nobr id="d1"></nobr></p>
</div>


</body>
<script type="text/javascript">
    // 绑定上传按钮
    $('#upFileBtn').click(function () {
        var formFile = new FormData($('#uploadForm')[0])
        $.ajax({
            url: "/detector", // 选择给定路由
            type: "POST",   // 选择上传方式
            data: formFile, // 使用form表单的形式上传
            processData: false,
            contentType: false,
            success: function (data) {
                var d = JSON.parse(data) // 解析JSON数据
                $('#img').attr('src', d.file_url); // 更新显示的图片
                $('#d1').html(d.detect_result) // 更新识别的结果
            }
        })
    })
</script>
</html>
```



效果展示如下

![image-20220829001055371](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220829001055371.png)

![image-20220829001217303](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220829001217303.png)

### 完成



```python
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask import Flask, request
from Mnist_detect import detect
import json

app = Flask(__name__)

app.config["UPLOADED_PHOTOS_DEST"] = 'uploads'

photo = UploadSet('photos', IMAGES)
configure_uploads(app, photo)
patch_request_class(app)

@app.route('/detector', methods=['POST'])
def detector():
    filename = photo.save(request.files['file']) #保存图片
    file_url = photo.url(filename) # 获取url
    path = photo.path(filename) # 获取存储路径
    result = detect(path)
    data = {'file_url': file_url, "detect_result": str(result)} # 构造返回数据
    data = json.dumps(data) # 转换为字符串
    return data

# 这是手写数字获取检测结果的途径
```

```python

@app.route('/post_test', methods=['POST'])
def post_test():
    # 获取json类型数据
    data = request.get_json()  # dict
    print(data)
    da = {"a": 1, "b": 2}
    da = json.dumps(da)
    return da

```







先有一个模型检测器函数，功能，传入一张待测图片，传出已测图片。



后端，调用检测函数实现检测，具体为，获取图片路径，将图片传入函数，得到已测图片的存放路径，上传已测图片。



```python
import time

import cv2
import numpy as np
from PIL import Image

from yolo import YOLO

@torch.no_grad()
def detect(img_path):
    img = img_path
    



```



是在太可恶了！居然迷惑我这么久，现在就让我们揭开前后端通信的面纱吧！

这里讲的是在web上展示本机的图片，并得到预测后的效果图。

1. 在web上选择本机文件夹里的图片，前端接收到路径，通过ajax传到后端，后端存图片，生成url，并检测图片，得到检测结果，在本地保存，将图片url和保存结果的图片url返回前端，前端展示在web上。传输的数据为json格式的数据。

如下面展示：

![image-20220902135541674](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220902135541674.png)

![image-20220902135527854](C:\Users\Happy\AppData\Roaming\Typora\typora-user-images\image-20220902135527854.png)







```
<script type="text/javascript">
    // 绑定上传按钮
    $('#result_file').click(function () {
        var formFile = new FormData($('#uploadForm')[0])
        $.ajax({
            url: "/detector", // 选择给定路由
            type: "POST",   // 选择上传方式
            data: formFile, // 使用form表单的形式上传
            processData: false,
            contentType: false,
            success: function (data) {
                var d = JSON.parse(data) // 解析JSON数据
                $('#img').attr('src', d.file_url); // 更新显示的图片
                $('#d1').html(d.detect_result) // 更新识别的结果
            }
        })
    })

```



















