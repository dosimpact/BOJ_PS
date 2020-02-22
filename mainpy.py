
import sys


def input(): return sys.stdin.readline().rstrip()


memo = {}

N = int(input())

memo[1] = ['1', '2', '3']

for i in range(2, N+1):
    # make i list
    ilist = []
    # 각 1번 메모에서 꺼내와서 1짜리 되는지 | 되면 추가
    for m in memo[i-1]:
        for j in ['1', '2', '3']:  # 1,2,3 을 붙여볼꺼임
            tmp = m+j
            isposs = True
            for k in range(1, i//2 + 1):  # 길이 1로 겹치나, 길이 2로 겹치나 확인 | 안겹치면 메모에 추가하기
                if tmp[-k:] == tmp[-2*k:-k]:
                    # if tmp[:-(k+1):-1] == tmp[-(k+1):-(k+1+k):-1]:
                    isposs = False
            if isposs:
                ilist.append(tmp)
    memo[i] = ilist
print(min(memo[N]))
