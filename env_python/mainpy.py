

import numpy as np


array1 = np.array([7, 2, 9, 10])
print(array1)  # [ 7  2  9 10]
print(type(array1))
print(array1.ndim)  # 1 1차원이다.
print(array1.shape)  # (4,)  4개의 원소

array2 = np.array([[5, 23, 45], [2.1, 2, 3]])
print(array2)
print(array2.ndim)  # 2차원이다.
print(array2.shape)  # (2,3) 2개의 원소 , 각각에는 3개의 원소

array3 = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]]])
print(array3)
print(array3.ndim)  # 3  3차원이다.
print(array3.shape)  # (2, 3, 3) 2 개의 원소 , 각각에는 3개의 원소, 그 속에는 3개의 원소


# ndarray
