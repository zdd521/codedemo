# bug

## cv2.log

### 错误：

cv2.log出现如下错误：

```python
data = np.array([[1, 2, 3], [1, 2, 3]])
new_data = np.array([[1, 2, 3], [1, 2, 3]])
temp_data = cv.log(data)
print(temp_data)

```

**error: (-215:Assertion failed) depth == CV_32F || depth == CV_64F in function 'cv::log'**

### 解决方案

数据问题，最直接的解决方法是，给图像除以或者乘以一个1.0

如下

```python
data = np.array([[1, 2, 3], [1, 2, 3]])
new_data = np.array([[1, 2, 3], [1, 2, 3]])
temp_data = cv.log(data*1.0)
print(temp_data)
```

结果：

```
[[0.         0.69314718 1.09861229]
 [0.         0.69314718 1.09861229]]
```
