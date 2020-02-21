
import sys


def input(): return sys.stdin.readline().rstrip()


# 입력처리
T = int(input())
for i in range(T):
    N = int(input())
    stu = list(map(int, input().split()))
    ans = [0 for _ in range(N+1)]
    for j in range(1, N+1):  # 1번학생이 탐색시작
        if(ans[j] == 1):
            continue
        check = [0 for _ in range(N+1)]
        check[j] = 1
        nxt = stu[j-1]
        while(True):
            # 다음학생이 다시 나인경우 ->가능 | 다음 학생이 check가 되있는경우 팀플실패 | 다음 학생이 check안되면 check후 계속
            if nxt == j:
                for i in range(N+1):
                    ans[i] = ans[i] | check[i]
                break
            if check[nxt] == 1:
                break
            if check[nxt] == 0:
                check[nxt] = 1
                nxt = stu[nxt-1]
    print(ans.count(0)-1)

"""
그리디 알고리즘 : 역으로 생각해서, 접근!

1.무조건 책을 한번에 많이 가져다 두는게 이득
2. 제일 먼 거리 책은 마지막에 하는게 이득

"""
