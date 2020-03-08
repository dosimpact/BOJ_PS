import copy


def move(arr):
    tmp = copy.deepcopy(arr)
    print(tmp, arr)
    arr[0] = 1
    print(tmp, arr)


move([5, 2, 3, 4])
"""

[5, 2, 3, 4] [5, 2, 3, 4]
[5, 2, 3, 4] [1, 2, 3, 4]

"""
