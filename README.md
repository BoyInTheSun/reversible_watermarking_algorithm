# 可视化可逆水印
实现了论文[Border following–based reversible watermarking algorithm for images with resistance to histogram overflowing](https://journals.sagepub.com/doi/10.1177/1550147720917014)中算法，并实现可视化。
## 边界追踪
传入原始图片。
通过论文中的边界追踪(Borader following)算法计算出边界。其中包括转化为灰度图、用大津算法计算出阈值、向外用0填充一像素、找边界、裁剪填充的最外1像素。
传出以边界像素数量大小排列前三的边界坐标，格式为：{}

## 水印嵌入

边界追踪算法将图片分割成几个部分（例如分为ABC三块），并以各部分分左上角像素点的坐标作为标记。利用论文中的相关算法得出能够嵌入信息最多的一块，通过直方图位移将信息嵌入。

## 水印提取

嵌入方将信息嵌入后的图片发送给接收方，同时发送嵌入块的标记信息及其峰值、最小点。

提取方再次对载体图像进行边界追踪，得到与嵌入信息前一致的边界信息与分块，通过接收到的标记信息判断出秘密信息嵌入在哪个块，并根据峰值与最小点进行信息还原。


## 可视化

# 用到的库
`openCV`和`QT5`
```shell
pip install opencv-python==4.4.0.44
pip install pyqt5==5.15.1
```
# 参考文献