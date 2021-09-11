# 슬라이딩 윈도우
# 최고의 이슈 검색어
# n일동안 최소k번 이상 검색 ( 연속)
# && n일동안 총 2*n*k번 이상 검색 (검색양?)
# n,k = 3,50
# 3일동안, 매일 50번 이상 검색, 해당 기간동안 300번 이상 검색
# 이 중에서 최고의 이슈 검색 고르기 ( 사전순 )

# eg1)
# n,k = 2,2
# 2일동안, 매일 2번 이상 검색
# 2일동안, 총 8번 충족

N, K = None, None
Table = dict()
Table_seq = dict()
Table_cnt = dict()
Table_ans = dict()
DAY = None


def window_seq(key):
    if key not in Table_seq:
        Table_seq[key] = [0 for _ in range(DAY)]
    # 연속성을 구하는 배열

    # 그날 K 번 이상 검색되었다면, 이전 +1 아니라면, 초기화
    for today in range(DAY):  # n,k = 2,1
        if today >= 1:
            Table_seq[key][today] = Table_seq[key][today-1]
        if Table[key][today] >= K:
            Table_seq[key][today] += 1
        else:
            Table_seq[key][today] = 0
    # print("Table_seq", Table_seq)


def window_cnt(key):  # n,k = 2,1
    if key not in Table_cnt:
        Table_cnt[key] = [0 for _ in range(DAY)]
    if key not in Table_ans:
        Table_ans[key] = [0 for _ in range(DAY)]
    # 횟수를 구하는 배열
    limit = 2*N*K
    # 슬라이딩 윈도우로, n일동안 K번 검색이 되는지
    start = 0
    sumState = 0
    for today in range(DAY):  # 0,1
        # 윈도우 오른쪽 증가
        sumState += Table[key][today]
        Table_cnt[key][today] += sumState  # 0 일차 검색어 (2)를 더한 경우
        if Table_seq[key][today] >= N and Table_cnt[key][today] >= limit:
            Table_ans[key][today] = 1
        # 윈도우 크기 왼쪽 감소 처리
        win_len = today - start + 1
        if win_len >= N:  # 0 - 0 + 1  크기 1 , N = 2
            sumState -= Table[key][start]
            start += 1
    # print("Table_cnt", Table_cnt)
    # print("Table_ans", Table_ans)


def getANS():
    ans_dict = dict()
    ans_maxCount = 0
    for key, value in Table_ans.items():
        ans_dict[key] = value.count(1)
        ans_maxCount = max(ans_maxCount, ans_dict[key])
    result = []
    for key, value in ans_dict.items():
        if ans_maxCount != 0 and value == ans_maxCount:
            result.append(key)
    result.sort()
    # print("result", result)
    if len(result) == 0:
        return "None"
    return result[0]


def solution(research, n, k):
    # research 순회하면서, dict에 key값으론,검색어 만들기
    # x : [2,2,0]    # y : [2,3,1]  # z : [0,0,1]
    global N, K, DAY
    N, K = n, k
    DAY = len(research)
    for today, words in enumerate(research):
        for key in list(words):
            if key not in Table:
                Table[key] = [0 for _ in range(DAY)]
            Table[key][today] += 1
    print(Table)
    for key in Table:
        window_seq(key)
        window_cnt(key)
    return getANS()


# print(solution(["abaaaa", "aaa", "abaaaaaa", "fzfffffffa"], 2, 2))
# print(solution(["yxxy", "xxyyy", "yz"], 2, 1))
print(solution(["xy", "xy"], 1, 1))
