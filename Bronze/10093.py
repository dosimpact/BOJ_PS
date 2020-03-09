import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

n = min([N, M])
m = max([N, M])
if m - n == 0:
    print(0)
    sys.exit(0)
print(m-n-1)
for i in range(n+1, m):
    print(i, end=" ")

"""
- 끝점 파악
만약 두수 사이의 정수가 없다면 ? 
무조건 두수 사이의 정수의 갯수는 m - n -1 일까?
 
"""
