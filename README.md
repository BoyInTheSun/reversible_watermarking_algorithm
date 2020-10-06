# 可视化可逆水印

实现了论文[Border following–based reversible watermarking algorithm for images with resistance to histogram overflowing](https://journals.sagepub.com/doi/10.1177/1550147720917014) 中算法，并实现可视化。

## 边界追踪

传入通过`opencv`读取的原始图片，格式为`numpy`三维数组，分别为长、宽、RGB值，类型为`uint8`。

通过论文中的边界追踪(Borader following)算法计算出边界。其中包括转化为灰度图、用大津算法计算出阈值、向外用0填充一像素、找边界、裁剪填充的最外1像素。

传出以一个列表，其中每个元素为`numpy`三维数组，分别为长、宽、RGBA值，类型为`uint8`，A。其代表若干个已切分的块，以可嵌入信息从大到小排列（若相同则以边界最左一列的最上一点坐标作为特征，以其横坐标从大到小排序，若再相同则对比纵坐标）。排除内部点小于等于2的边界。

#### 关于如何判断内部点的多少

由于需要对内部没有可用点的分块进行筛除，则应判断分块内部点的多少。

考虑到若使用 “ 记录所有边界的坐标值然后判断某点的坐标值是否在其范围内来确定该点是否在边界内部 ” 的方法，会有增大存储量、占用较大空间、且难以判断的问题出现，我们提出了新的想法：

筛去除分块外的背景 → 将边界内部标记为3 → 再次扫描时通过标记是否为3判断内外部

其中，“筛去出分块外的背景” 一步中，我们参考并改进了OpenCV库中的floodfill()算法，以类似的方式标出了无用背景，并做了筛除。

同时，在“将边界内部标记为3” 一步中，优化了边界的标记方式，内部点数极少的分块不做标记（以Lena图为例，优化前边界追踪循环为134轮，优化后为117轮）很大程度上减少了后续的工作量。

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