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

ansMax = None  # 라이언이 얻을 최대 점수 값
ansScoreList = None
INFO = None  # 어피치 화살 정보
scoreList = None  # 라이언 재귀 함수 상태

# ❌ 라이언이 점수를 따면 어피치가 그만큼 못딴다.
# ❌ 점수 차이에 대해서 MAX 값임. if ansMax < cur_score:


def go(bullet, cur_score, nextIdx,  apeachScore):
    # 남은 화살 수, 딴 점수, 다음 과녁, 나의 점수셋
    global ansMax, ansScoreList
    # BASE - 더이상 맞출 과녁이 없는 경우
    if nextIdx >= len(INFO) or bullet == 0:
        if apeachScore >= cur_score:
            return
        elif apeachScore < cur_score:
            if ansMax < cur_score - apeachScore:
                ansMax = cur_score - apeachScore
                ansScoreList = deepcopy(scoreList)
        return
    # BASE - 더이상 쏠 화살이 없는 경우
    # -- 점수 갱신
    if bullet >= INFO[nextIdx]+1:
        plusScore = 10 - nextIdx
        scoreList[nextIdx] = INFO[nextIdx]+1
        if INFO[nextIdx]+1 == 1:  # 어피치 안무시
            go(bullet - (INFO[nextIdx]+1), cur_score + plusScore,
               nextIdx+1, apeachScore)
        else:  # 어피치 무시
            go(bullet - (INFO[nextIdx]+1), cur_score + plusScore,
               nextIdx+1, apeachScore - plusScore)
        scoreList[nextIdx] = 0
    go(bullet, cur_score, nextIdx+1,  apeachScore)


def solution(n, info):
    global INFO, ansMax,  scoreList, ansScoreList
    ansScoreList = [-1]
    INFO = info
    # 라이언 점수, 점수 셋, 어피치 점수
    ansMax = -1
    scoreList = [0 for _ in range(11)]
    apeachScore = 0
    for idx, e in enumerate(info):
        if e != 0:
            apeachScore += (10 - idx)
    go(n, 0, 0, apeachScore)
    return ansScoreList


# 10점부터 0점까지
print(
    solution(5	, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
)


"""
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.57ms, 10.4MB)
테스트 3 〉	통과 (0.62ms, 10.3MB)
테스트 4 〉	통과 (0.23ms, 10.3MB)
테스트 5 〉	통과 (0.63ms, 10.3MB)
테스트 6 〉	통과 (0.62ms, 10.2MB)
테스트 7 〉	통과 (0.22ms, 10.3MB)
테스트 8 〉	통과 (0.10ms, 10.2MB)
테스트 9 〉	통과 (0.23ms, 10.3MB)
테스트 10 〉	통과 (0.09ms, 10.2MB)
테스트 11 〉	통과 (0.16ms, 10.3MB)
테스트 12 〉	통과 (0.15ms, 10.3MB)
테스트 13 〉	통과 (0.42ms, 10.4MB)
테스트 14 〉	통과 (0.51ms, 10.2MB)
테스트 15 〉	통과 (0.57ms, 10.3MB)
테스트 16 〉	통과 (0.30ms, 10.3MB)
테스트 17 〉	통과 (0.25ms, 10.2MB)
테스트 18 〉	통과 (0.05ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	실패 (0.55ms, 10.3MB)
테스트 21 〉	실패 (0.51ms, 10.3MB)
테스트 22 〉	실패 (0.65ms, 10.3MB)
테스트 23 〉	통과 (0.08ms, 10.3MB)
테스트 24 〉	실패 (0.72ms, 10.3MB)
테스트 25 〉	실패 (0.73ms, 10.5MB)
"""
