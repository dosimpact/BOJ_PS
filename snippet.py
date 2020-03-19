

now = [7, 2, 3, 6, 5, 4, 1]

# 완료된 순열은 완전 내림차순이다.


def next_permutation(arr: []):
    i = len(arr)-1
    while i > 0 and arr[i-1] > arr[i]:
        i -= 1
    if i == 0:
        return False
    j = len(arr) - 1
    while arr[i-1] > arr[j]:
        j -= 1
    (arr[i-1], arr[j]) = (arr[j], arr[i-1])
    j = len(arr) - 1
    while i < j:
        (arr[i], arr[j]) = (arr[j], arr[i])
        i += 1
        j -= 1
    return True


print(now)
next_permutation(now)
print(now)
