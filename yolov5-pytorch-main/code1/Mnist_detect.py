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


# if __name__ == '__main__':
#     result = detect(img_path='D:\shuqikaohe\yolov5-pytorch-main\code1\data\picture/1.jpg')
#     print(result)
