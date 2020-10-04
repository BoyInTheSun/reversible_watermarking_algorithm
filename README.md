# 可视化可逆水印
实现了论文[Border following–based reversible watermarking algorithm for images with resistance to histogram overflowing](https://journals.sagepub.com/doi/10.1177/1550147720917014)中算法，并实现可视化。
## 边界追踪
传入原始图片。
通过论文中的边界追踪(Borader following)算法计算出边界。其中包括转化为灰度图、用大津算法计算出阈值、向外用0填充一像素、找边界、裁剪填充的最外1像素。
传出以边界像素数量大小排列前三的边界坐标，格式为：{}

## 水印嵌入

## 水印提取

## 可视化

# 用到的库
`openCV`和`QT5`
```shell
pip install opencv-python==4.4.0.44
pip install pyqt5==5.15.1
```
# 参考文献