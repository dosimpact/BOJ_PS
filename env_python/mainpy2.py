from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)

fi = [0 for _ in range(31)]
fi[2] = 1
fi[3] = 1
for i in range(4, 31):
    fi[i] = fi[i - 1] + fi[i - 2]  # 4일째의 b 변수

# 떡 갯수, 어제 + 그저깨
# 1,2,3,5,8,13
# 오늘 준 갯수와 몇일인지
# 첫날 둘째날에 준 떡의 수를 구해라

D, K = map(int, input().split())
ac, bc = 1, 1
if D >= 4:
    ac, bc = fi[D - 1], fi[D]
tmp_a, tmp_b = 1, 1

while True:
    res = ac * tmp_a + bc * tmp_b
    if res == K:
        print(tmp_a)
        print(tmp_b)
        break
    if res > K:
        tmp_a += 1
        tmp_b = 1
    tmp_b += 1
