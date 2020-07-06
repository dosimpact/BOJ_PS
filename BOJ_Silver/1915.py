import sys
sys.setrecursionlimit(10*6)


def input(): return sys.stdin.readline().rstrip()


(N, M) = map(int, input().split())

# res = list(input())
# print(res)
Board = [list(map(int, list(input()))) for _ in range(N)]

d = [[0 for _ in range(M)] for _ in range(N)]

Ans = 0
for i in range(0, M):
    d[0][i] = Board[0][i]
    # Ans = max([Ans, d[0][i]]) FB) 처음줄의 d를 만드는데, 이것또한 답이 되는 경우가 있잖아.
for j in range(0, N):
    d[j][0] = Board[j][0]
    #Ans = max([Ans, d[j][0]])


for i in range(1, N):
    for j in range(1, M):
        if Board[i][j] == 1:
            d[i][j] = min([d[i-1][j], d[i][j-1], d[i-1][j-1]]) + 1
            Ans = max([Ans, d[i][j]])
print(Ans*Ans)


"""
FB) 처음줄의 d를 만드는데, 이것또한 답이 되는 경우가 있잖아.
"""
