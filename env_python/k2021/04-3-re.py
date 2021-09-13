from copy import deepcopy
from collections import defaultdict

# ❌ 라이언이 점수를 따면 어피치가 그만큼 못딴다.
# ❌ 점수 차이에 대해서 MAX 값임. if ansMax < cur_score:
N, Info = None, None
ansDiff, ansMyInfo = None, None
ansMyInfoList = defaultdict(list)
# 어피치의 점수 , 나의 점수

# 나의 총알 ..


def go(bullet, nextIdx, MyScore, apeachScore, myInfo):
    global ansDiff, ansMyInfo

    # END CASE : 총알 바닥이거나, 끝까지 도달
    if bullet <= 0 or nextIdx >= 11:
        # print(f" myInfo {myInfo}")
        final_diff = MyScore - apeachScore
        if final_diff > 0 and ansDiff <= final_diff:
            # print(f"final_diff {final_diff} myInfo--->", myInfo)
            ansDiff = final_diff
            ansMyInfo = deepcopy(myInfo)
            ansMyInfoList[final_diff].append(ansMyInfo)

        return
    # -- 특별 예외 케이스
    if nextIdx == len(Info) - 1:
        curr_score = 10 - nextIdx
        copyMyInfo = deepcopy(myInfo)
        copyMyInfo[nextIdx] = bullet
        go(0, nextIdx + 1, MyScore, apeachScore, copyMyInfo)
    # GO 현재 점수를 맞추는 경우
    # -- 총알 여유가 있어야함
    # -- 어피치를 무시하는 경우
    if bullet >= Info[nextIdx] + 1:
        need_bullet = Info[nextIdx] + 1
        next_bullet = bullet - need_bullet
        curr_score = 10 - nextIdx
        copyMyInfo = deepcopy(myInfo)
        copyMyInfo[nextIdx] = need_bullet
        if need_bullet == 1:  # 1개만 필요한 경우 ( 어피치를 무시안함 )
            go(next_bullet, nextIdx + 1, MyScore +
               curr_score, apeachScore, copyMyInfo)
        else:
            go(next_bullet, nextIdx + 1, MyScore +
               curr_score, apeachScore - curr_score, copyMyInfo)
    # GO 아닌 경우
    copyMyInfo = deepcopy(myInfo)
    go(bullet, nextIdx+1, MyScore, apeachScore, copyMyInfo)


def solution(n, info):
    global N, Info, ansDiff, ansMyInfo
    N, Info = n, info
    ansDiff, ansMyInfo = 0, [-1]
    apeachScore = 0
    for idx, e in enumerate(info):
        if e != 0:
            apeachScore += (10-idx)
    go(n, 0, 0, apeachScore, [0 for _ in range(len(info))])

    if len(ansMyInfoList.keys()) == 0:
        return [-1]
    # print(ansMyInfoList)
    maxDiff = max(ansMyInfoList.keys())
    ansMyInfoList[maxDiff].sort(key=lambda x: (
        x[-1], x[-2], x[-3], x[-4], x[-5], x[-6], x[-7], x[-8], x[-9]
    ))
    # print(ansMyInfoList[maxDiff])
    return ansMyInfoList[maxDiff][-1]


# 10점부터 0점까지
# print(
#     solution(5	, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
# )

print(
    solution(9	, 	[0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])
)

# print(
#     solution(10	, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])
# )
