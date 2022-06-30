## 创建一个git本地与远程仓库

- 这边默认已经有github的帐号了-.-

首先来到本地的磁盘，找一个你想放你的项目的新目录

如：

- ![](D:\summer_assessment\picture\1-1.png)https://github.com/yuanxiao7/summer_project/commit/b88e41f6458738dee7b6d0d0d7b16c16c532da7c

这里只是给个空目录示范一下。temp为你的文件名，随意，最好用英文的，毕竟windows用中文路径的中会有一些小bug。

然后你就右击鼠标，在菜单栏点击Git Bash Here进入git命令行如下：

- ![](D:\summer_assessment\picture\1-2.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/1-2.png

​	然后输入git init 回车，即可在该目录下创建一个本地仓库，你就会在对应的目录看到一个.git文件（注意，这是个隐藏文件）

- ![](D:\summer_assessment\picture\1-3.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/1-3.png

- 打开隐藏文件，在文件扩展名处打勾即可
- ![](D:\summer_assessment\picture\1-4.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/1-5.png

接下来就简单创建一个readme.md文件，上传

- 在命令行输入
- git add readme.md
- git commit -m "First file.(这里解释一下上传的文件是什么)"

到此，本地的上传就完成了，接下来到你的github页面，创建一个新的仓库为远程仓库

- ![](D:\summer_assessment\picture\1-5.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/1-5.png

点击 repository--》new 然后就转到一个页面，填写仓库名称，写点小解释回车就建好了，点进新仓库来到如下界面，这里就会有解释，如何在本地创建仓库并连接到远程仓库。

- ![](D:\summer_assessment\picture\repository_picture1.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/repository_picture1.png

- ![](D:\summer_assessment\picture\repository_picture2.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/repository_picture2.png

然后你就接着上面的命令，跟着他敲命令就好，可能你敲到git branch -M main会出现提示找不到，那我们就不用https改用ssh的链接（它默认主分支是main但我们这里用ssh所以就改为master分支）下方箭头出即分支处。

- ![](D:\summer_assessment\picture\1-7.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/1-7.png

- ![](D:\summer_assessment\picture\1-6.png)https://github.com/yuanxiao7/summer_project/blob/master/picture/1-6.png

然后就照着git push会出现error然后你就照着他的解决方案给的命令再push一遍就好。（这里忘记截图了）

然后就到你的GitHub上刷新一下，点击分支，点击master看到你刚刚传上来的readme.md文件，就欧克了！快去把你的项目上传吧！

