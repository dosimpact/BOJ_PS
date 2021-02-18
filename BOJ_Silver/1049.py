import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 1049

N, M = map(int, input().split())

B_Set = []
B_Sep = []
for _ in range(M):
    t, p = map(int, input().split())
    B_Set.append(t)
    B_Sep.append(p)


Sep_val = min(B_Sep)  # 단가 구매 가격 ( 2순위 )
Set_val = min(B_Set)  # 6개 이상 구매시 , 세트 구매가격 ( 1순위 )

Set_cnt, Sep_cnt = divmod(N, 6)

if Set_val / 6 >= Sep_val:  # 무조건 개별이 이득인 경우
    # print("무조건 개별이득")
    print(N*Sep_val)
elif Set_val <= Sep_val:  # 무조건 세트가 이득인 경우
    # print("무조건 세트 이득")
    ans = Set_cnt * Set_val
    if Sep_cnt > 0:
        ans += Set_val
    print(ans)
else:  # 혼합으로 사야 이득인 경우
    # print("혼합")
    h = Set_val // Sep_val
    h += 1
    if Sep_cnt >= h:
        print(Set_val*(Set_cnt+1))
    else:
        print(Set_val*Set_cnt + Sep_val*Sep_cnt)

"""
import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

first_arr = sorted(arr, key=lambda k: k[0])
second_arr = sorted(arr, key=lambda k: k[1])
answer = min(
    ((n//6) + 1) * first_arr[0][0],
    (n//6) * first_arr[0][0] + (n % 6) * second_arr[0][1],
    n * second_arr[0][1]
)
print(answer)
"""
