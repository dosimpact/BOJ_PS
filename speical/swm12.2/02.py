
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 무한 회로 N개의 발판
# 각 발퍈 양의 정수 음의 정수
# 발판 밟으면 해당 숫자만큼 좌 우 이동
# 음수 왼 , 양수 오른쪽 ( 0은 없음! )
# 마주할 수 있는 모든 무한 회로중 가장 긴 무한 회로...

# 시작 점이 1번 ~ 10번 전부 다임
# 그떄마다 DFS탐색을 통해서 이미 방문 했더라면 그 숫자를 빼자.
# check = check +1 , if check > check i - check j = 1번시작 무한 회로 길이

N, data = None, None
check = None
ansList = []


def DFS(now: int, step: int):
    # print(f"now,step {now,step}")
    # basecase - 이미 밟은 경우
    # 더 밝을 수 있는 경우
    nxt = (now + data[now]) % N
    if check[nxt]:
        return (step+1) - check[nxt]
    else:
        check[nxt] = step+1
        return DFS(nxt, step+1)


def main():
    global N, data, check
    N = int(input())
    data = list(map(int, input().split()))
    for i in range(N):
        check = [0 for _ in range(N)]
        check[i] = 1
        ansList.append(DFS(i, 1))
        # print(check)
        # print(f"res {res}")
    print(max(ansList))


if __name__ == "__main__":
    main()


"""
10
3 5 -1 -2 4 4 3 -2 -3 -2
>3

3
1 1 1
>3

4
3 -1 1 -3
>2

4
1 1 1 1
>4

"""


# 메모지 얘기가 나왔다. 1분 더 걸리나?
