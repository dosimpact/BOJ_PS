

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
    [[1, 2, 3], [4, 5, .16], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]]])
print(array3)
print(array3.ndim)  # 3  3차원이다.
print(array3.shape)  # (2, 3, 3) 2 개의 원소 , 각각에는 3개의 원소, 그 속에는 3개의 원소
print(array3.dtype)  # float64

# ndarray

# 타입 지정

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int)
print(arr1, arr1.dtype)
print(arr2, arr2.dtype)

# 타입 변환 -> 메모리절약을 위해 주로 사용


array_int = np.array([1, 2, 3, ])
array_float = array1.astype('float64')
print(array_int.dtype, array_float.dtype)  # int32 float64


# axis 기반 연산

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3.sum())
print(arr3.sum(axis=0))  # [5 7 9]
print(arr3.sum(axis=1))  # [ 6 15]


# ndarray 편리한 생성 : arrange, zeros, ones

# arrange(): 연속값을 요소로 가지는 ndarray 생성
# zeros(): 0으로 초기화된 ndarray 생성
# ones(): 1으로 초기화된 ndarray 생성

arr4 = np.arange(10)  # 0부터 9까지 들어감
print(arr4)  # [0 1 2 3 4 5 6 7 8 9]
arr5 = np.zeros((4, 3), dtype='int32')
print(arr5)  # 4개원소 각각 3개의 원소가, 있어, 다 0이야.
arr6 = np.ones((4, 3), dtype='int32')
print(arr6)  # 4개원소 각각 3개의 원소가, 있어, 다 1이야.


# ndarray - 차원 크기 변경 : reshape()


arr7 = np.arange(10)
print(arr7)
arr7 = arr7.reshape(2, 5)
"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""
print(arr7)
arr7 = arr7.reshape(5, 2)
print(arr7)
"""
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
"""

arr7 = arr7.reshape(-1, 5)  # 몇개의 덩어든, 5개씩 묶어.
print(arr7)
"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""
arr7 = arr7.reshape(5, -1)  # 5개의 덩어리도 만들어, 몇개씩 들어있는지는 몰라.
print(arr7)
"""
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
"""
arr7 = arr7.reshape(-1, 1) 
print(arr7)
"""
[[0]
 [1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
"""
arr7 = arr7.reshape(-1, )  # flatten
print(arr7)  # [0 1 2 3 4 5 6 7 8 9]
