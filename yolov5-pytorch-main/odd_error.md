## Descriptors cannot not be created directly.

sudo+ssh://lcx@172.25.6.99:22/home/lcx/miniconda3/envs/hlh_torch10.2/bin/python3.8 -u /home/lcx/shuqikaohe/train.py
Traceback (most recent call last):
  File "/home/lcx/shuqikaohe/train.py", line 18, in <module>
    from utils.callbacks import LossHistory, EvalCallback
  File "/home/lcx/shuqikaohe/utils/callbacks.py", line 9, in <module>
    from torch.utils.tensorboard import SummaryWriter

​    _descriptor.FieldDescriptor(
  File "/home/lcx/miniconda3/envs/hlh_torch10.2/lib/python3.8/site-packages/google/protobuf/descriptor.py", line 560, in __new__
​    _message.Message._CheckCalledFromGeneratedFile()
TypeError: Descriptors cannot not be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:

 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates

解决： 按提示下载更低版本的protobuf



## 使用vim文本编辑器

先 cd 来到所要修改文件的根目录，之后再 vim + filename 进入文件，在你进入insert模式的前一页面就是正常模式，然后就可以根据百度教程修改了，保存后退出是，先按 ESC 键回到正常状态，再按一次，然后输入 :wq 回车 即可退出文件，具体操作如下：

update-alternatives: 使用 /usr/bin/vim.basic 来在自动模式中提供 /usr/bin/ex (ex)
正在处理用于 man-db (2.8.3-2ubuntu0.1) 的触发器 ...
(hlh_torch10.2) lcx@lcx:~$ vim utils_fit.py
(hlh_torch10.2) lcx@lcx:~$ (hlh_torch10.2) lcx@lcx:~$
(hlh_torch10.2) lcx@lcx:~$ conda deactivate
(base) lcx@lcx:~$ cd
(base) lcx@lcx:~$ cd shuqikaohe
(base) lcx@lcx:~/shuqikaohe$ cd
(base) lcx@lcx:~$ ll
总用量 188

... file list ...

(base) lcx@lcx:~$ cd shuqikaohe
(base) lcx@lcx:~/shuqikaohe$ cd yolov5-pytorch-main
-bash: cd: yolov5-pytorch-main: 没有那个文件或目录
(base) lcx@lcx:~/shuqikaohe$ cd utils
(base) lcx@lcx:~/shuqikaohe/utils$ ll
总用量 128

... file list ...

(base) lcx@lcx:~/shuqikaohe/utils$ vim utils_fit.py
(base) lcx@lcx:~/shuqikaohe/utils$



 
