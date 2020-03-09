import sys


def input(): return sys.stdin.readline().rstrip()


# def c_rotate(c: str):
#     return c[-1]+c[1:]


# def cwise_rotate(c: str):
#     return c[1:]+c[-1]
def c_rotate(c: str):
    return c[-1]+c[:-1]


def cwise_rotate(c: str):
    return c[1:]+c[0]


def rot(c: str, di: int):
    if di == 1:
        return c_rotate(c)
    elif di == -1:
        return cwise_rotate(c)


tupNum = int(input())
tup = [input() for _ in range(tupNum)]
# print(tup)


k = int(input())
for _ in range(k):
    num, di = map(int, input().split())
    num -= 1
    dilist = [0 for _ in range(tupNum)]
    # 각 원소에 돌아갈 방향을 넣자. [ ] 0 안돌아, 1 시계방향 , -1 반시계 방
    dilist[num] = di
    # 오른쪽 부터 조사
    for i in range(num+1, tupNum):
        # 톱니의 극이 다르면 # 돌아갈 극의 반대로 저장
        if tup[i-1][2] != tup[i][6]:
            dilist[i] = -dilist[i-1]
        else:
            break
    # 오른쪽 부터 조사
    for i in range(num, 0, -1):
        # 톱니의 극이 다르면 # 돌아갈 극의 반대로 저장
        if tup[i-1][2] != tup[i][6]:
            dilist[i-1] = -dilist[i]
        else:
            break
    # print(dilist)
    for i, di in enumerate(dilist):
        if di != 0:
            tup[i] = rot(tup[i], di)
    # print(tup)

# print(tup)
Ans = 0

for i in range(0, tupNum):
    if tup[i][0] == '1':
        Ans += 1
print(Ans)
"""
톱니바퀴 4종 입력완료

"""
