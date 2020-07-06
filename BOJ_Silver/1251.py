"""
2966
"""


import sys


def input(): return sys.stdin.readline().rstrip()


def procress(s1: [], s2: [], s3: []):
    i = 0
    j = len(s1)-1
    while i < j:
        s1[i], s1[j] = s1[j], s1[i]
        i += 1
        j -= 1

    i = 0
    j = len(s2)-1
    while i < j:
        s2[i], s2[j] = s2[j], s2[i]
        i += 1
        j -= 1

    i = 0
    j = len(s3)-1
    while i < j:
        s3[i], s3[j] = s3[j], s3[i]
        i += 1
        j -= 1

    return "".join(s1)+"".join(s2)+"".join(s3)


ans = list(input())

ansList = []

for i in range(len(ans)):
    for j in range(i+1, len(ans)):
        s1 = ans[:i]
        s2 = ans[i:j]
        s3 = ans[j:]
        if len(s1) >= 1 and len(s2) >= 1 and len(s3) >= 1:
            #print(s1, s2, s3)
            res = procress(s1, s2, s3)
            # print(res)
            ansList.append(res)

ansList.sort()
print(ansList[0])
