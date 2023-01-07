# bug

## np.log

### 错误：

np.log出现如下警告：

```python
data = np.array([[1, 2, 3], [1, 0, 3]])
temp_data = np.log(data)
print(temp_data)
```

**RuntimeWarning: divide by zero encountered in log**

### 错误原因

log运算，指数为0的情况下，除了0的若干次方，没人任何数可以通过指数运算得到0

### 解决方案

一般这种问题是出现在对np.array做处理的情况中，主要存在于以下情形

1. 图像进行某种数据增强需要进行log运算
2. 某种公式复现需要log运算

一般而言这种问题是通过用最小数据来替换掉0值解决的，可以采用如下方法：


```python
import numpy as np

def replace_zeros(img):
    """

    :param img:
    :return:
    """
    min_no_zero = min(img[np.nonzero(img)])
    img[img == 0] = min_no_zero
    return img
```

示例如下：
```python
data = np.array([[1, 2, 3], [1, 0, 3]])
data = replace_zeros(data)
temp_data = np.log(data)
print(temp_data)
```

结果：
```
[[0.         0.69314718 1.09861229]
 [0.         0.         1.09861229]]
```

**具体参考:[github地址](https://github.com/ksks14/codedemo/blob/dev-lbs/bug/numpy/np_log.md)**