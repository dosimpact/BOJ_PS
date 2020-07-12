# Numpy 복습

- 파이썬에서 선형대수 기반의, 프로그래밍을 쉽게 할 수 있다.
- 반복문 없이 대량의 데이터의 배열 연산 가능 && 빠른 배열 연산속도 보장
- c/c++ 기반의 저 수준 언어 기반 API.

# basic create - np.array(),type(),ndim,shape,dtype

```python
import numpy as np

# basic create - np.array(),type(),ndim,shape,dtype

# 1차원 배열 만들기 | 타입,차원,shape확인
array1 = np.array([7, 2, 9, 10])
print(array1)  # [ 7  2  9 10]
print(type(array1))  # <class 'numpy.ndarray'>
print(array1.ndim)  # 1 1차원이다.
print(array1.shape)  # (4,)  4개의 원소

array2 = np.array([[5, 23, 45], [2.1, 2, 3]])
print(array2)
print(array2.ndim)  # 2차원이다.
print(array2.shape)  # (2,3) 2개의 원소 , 각각에는 3개의 원소

array3 = np.array(
    [[[1, 2, 3], [4, 5, 0.16], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]]]
)
print(array3)
print(array3.ndim)  # 3  3차원이다.
print(array3.shape)  # (2, 3, 3) 2 개의 원소 , 각각에는 3개의 원소, 그 속에는 3개의 원소
print(array3.dtype)  # float64
```
