
import sys
import math


def input(): return sys.stdin.readline().rstrip()


def bfs(who, count, Number):  # 누구냐, 몇번째냐, 컴포넌트번호는
    global stu, check, cnt
    if check[who] != 0:
        if Number == check[who]:
            return count - cnt[who]
        else:
            return 0

    # 처음 방문이면 | 컴포넌트 넘버 | 카운트
    check[who] = Number
    cnt[who] = count
    return bfs(stu[who], count+1, Number)


stu = []  # 학생정보
check = []  # 컴포넌트 번호
cnt = []  # n 방문
# 입력처리
T = int(input())
for i in range(T):
    N = int(input())

    stu = list(map(int, input().split()))
    stu.insert(0, 0)
    check = [0 for _ in range(N+1)]
    cnt = [0 for _ in range(N+1)]

    ans = N
    for i in range(1, N+1):
        if check[i] == 0:
            ans -= bfs(i, 1, i)
    print(ans)
    # 각 원소를 순회 | 방문하지 x 라면 방문 |

"""
단지 번호 붙이기 + 순회 찾기

"""
