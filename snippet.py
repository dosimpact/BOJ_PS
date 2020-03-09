

def minDist(arr, here, there):
    return min([abs((0+here) - there), abs((len(arr) + here) - there)])


def minDist_dir(arr, here, there1, there2):
    return -1 if (minDist(arr, here, there1) - minDist(arr, here, there2)) > 0 else 1


arr = [0, 0, 0, 0, 0, 0, 1, 0, 1]

print(minDist(arr, 2, 6))
print(minDist(arr, 2, 8))
print(minDist_dir(arr, 2, 6, 8))


"""
그리디 - 로테이팅
최소 로테이팅
"""

print(arr)
print(arr[::-1])
