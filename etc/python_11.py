
import time
import numpy as np
f"""
넘파이 sort()유형

- np.sort() 원본 유지, 정렬된 배열 반환
- ndarray.sort()  원본 자체를 정렬한다
"""
arr = np.array([4, 2, 1, 9])
print(arr)  # [4 2 1 9]

arr_sorted = np.sort(arr)
print(arr_sorted)  # [1 2 4 9]
print(arr)  # [4 2 1 9]


arr.sort()
print(arr)  # [1 2 4 9]

