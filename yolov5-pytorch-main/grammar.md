### %matplotlib inline

**%matplotlib inline** 用在Jupyter notebook中（代替plt.show()）； PyCharm中不支持，在PyCharm中去掉这个即可（用plt.show()代替图像的显示）。

- 注：%matplotlib inline 可以在Ipython编译器里直接使用，功能是可以内嵌绘图，并且可以省略掉plt.show()这一步。
- 注：而%matplotlib具体作用是当你调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候，可以直接在你的python console里面生成图像。



if classname.find('Conv') != -1:  **# find ()函数，实现查找classname中是否含有conv字符，没有返回-1；有返回0**.

 nn.init.normal_(m.weight.data, 0.0, 0.02)   #  m.weight.data 表示需要初始化的权重。
