"""
2858
"""


import sys


def input(): return sys.stdin.readline().rstrip()


R, B = map(int, input().split())  # 8`5 000 ,  1`2 000 000

for i in range(1, int(B**(1/2)+1)):  # 브라운 타일 넓이 -> 모든 가능한 변의 경우의수 -> 레드 타일의 갯수와 맞으면 -> 정답 출력
    if B % i == 0:
        x = i
        y = B // i
        if B == ((x+2)*(y+2) - R):
            print(max(x+2, y+2), min(x+2, y+2))
            exit(0)
