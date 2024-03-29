from copy import deepcopy
# 양궁대회
# 라이언 (지난우승자) vs 어피티(ruftmdwjs)
# 지난우승자 - 핸디켑
# -- 어피치 먼저 쏜다
# -- 10점을 , 라이언이 3발, 어피치가 2발이면, 라이언이 10점을 가져감
# -- 10점을 , 라이언이 2발, 어피치가 2발이면, 어피치가 10점을 가져감 ( 핸디캡 부분 )
# -- 최종 점수가 같은 경우 어피치 승 ( 핸디캡 부분 )

# 어피치는 다 쏜 상황
# 라이언이, 어떻게 쏴야 큰 점수로 이길지
# info 10점부터 0점까지

# 화살을 낭비하는건 의미가 없다. - 무조건 어피치보다 +1개 소비
# 재귀 + 백트레킹 ( 맞출래 안할래 ) (2)**(10) - 충분히 가능

ansSet = None
ansMax = None  # 라이언이 얻을 최대 점수 값
ansScoreList = None
INFO = None  # 어피치 화살 정보
scoreList = None  # 라이언 재귀 함수 상태

# ❌ 라이언이 점수를 따면 어피치가 그만큼 못딴다.
# ❌ 점수 차이에 대해서 MAX 값임. if ansMax < cur_score:


def go(bullet, cur_score, nextIdx, scoreSet, apeachScore):
    # 남은 화살 수, 딴 점수, 다음 과녁, 나의 점수셋
    global ansMax, ansSet, ansScoreList
    # print("cur_score", cur_score, "scoreSet", bin(scoreSet))
    # BASE - 더이상 맞출 과녁이 없는 경우
    if nextIdx >= len(INFO) or bullet == 0:
        if apeachScore >= cur_score:
            return
        elif apeachScore < cur_score:
            if ansMax < cur_score - apeachScore:
                ansScoreList = deepcopy(scoreList)
                ansMax = cur_score - apeachScore
                ansSet = scoreSet
        return
    # BASE - 더이상 쏠 화살이 없는 경우
    # -- 점수 갱신
    if bullet >= INFO[nextIdx]+1:
        if INFO[nextIdx]+1 == 1:  # 어피치 안무시
            scoreList[nextIdx] = INFO[nextIdx]+1
            plusScore = 10 - nextIdx
            go(bullet - (INFO[nextIdx]+1), cur_score + plusScore,
               nextIdx+1, scoreSet | (1 << plusScore), apeachScore)
            scoreList[nextIdx] = 0
        else:  # 어피치 무시
            scoreList[nextIdx] = INFO[nextIdx]+1
            plusScore = 10 - nextIdx
            go(bullet - (INFO[nextIdx]+1), cur_score + plusScore,
               nextIdx+1, scoreSet | (1 << plusScore), apeachScore - plusScore)
            scoreList[nextIdx] = 0
    go(bullet, cur_score, nextIdx+1, scoreSet, apeachScore)
    # GO - 과녁을 맞추는 경우
    # -- 어피치보다 더 많이 쏴야함


def listToSet(scoreList):
    return list(map(int, list(bin(scoreList))[2:]))


def solution(n, info):
    global INFO, ansMax, ansSet,  scoreList, ansScoreList
    ansScoreList = [-1]
    INFO = info
    # 라이언 점수, 점수 셋, 어피치 점수
    ansMax, ansSet,  = -1, 0
    scoreList = [0 for _ in range(11)]
    apeachScore = 0
    for idx, e in enumerate(info):
        if e != 0:
            apeachScore += (10 - idx)
    go(n, 0, 0, 0, apeachScore)
    return ansScoreList


# 10점부터 0점까지
print(
    solution(5	, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
)
