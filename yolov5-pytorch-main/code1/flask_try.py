from flask import render_template

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




















