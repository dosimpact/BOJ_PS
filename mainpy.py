import sys
sys.setrecursionlimit(10*6)


def input(): return sys.stdin.readline().rstrip()


N = int(input())  # 1 ~ N 까지 100
i = 5
Ans = 0
while(i <= N):
    Ans += int(N / i)
    i = i*5  # fb) i가 5의 배수씩 커지는 상황
print(Ans)
