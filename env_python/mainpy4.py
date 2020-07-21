import sys

input = sys.stdin.readline

LIMIT_N = 101
tcase = int(input())
X, Y = 0, 0
graph = [[0 for _ in range(LIMIT_N)] for _ in range(LIMIT_N)]
check_o = [[0 for _ in range(LIMIT_N)] for _ in range(LIMIT_N)]
check_1 = [[0 for _ in range(LIMIT_N)] for _ in range(LIMIT_N)]
check_2 = [[0 for _ in range(LIMIT_N)] for _ in range(LIMIT_N)]


# check type , start x , start y
def BFS(check, sx, sy):
    # global check_1, check_2, check_o
    pass


for _ in range(tcase):
    X, Y = map(int, input().split())
    for i in range(X):
        graph[i] = input()
    # for i in range(X):
        # print(*graph[i])

    # check_out BFS

    # check_1 BFS

    # check_2 BFs

    # find minial metting point
"""
3
5 9
****#****
*..#.#..*
****.****
*$#.#.#$*
*********
5 11
*#*********
*$*...*...*
*$*.*.*.*.*
*...*...*.*
*********.*
9 9
*#**#**#*
*#**#**#*
*#**#**#*
*#**.**#*
*#*#.#*#*
*$##*##$*
*#*****#*
*.#.#.#.*
*********
"""
