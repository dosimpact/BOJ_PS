# 뷸량 이용자
# 한번에 한명의 유저 신고
# - 신고횟수 제한 없음 , 동일유저 여러번은 1번만 처리
# K 번 이상 신고된 유저는 , 게시판 이용정지, 신고자한테 이메일
# - 정지해도 신고는 가능


def solution(id_list, report, k):
    answer = []
    # 유저 key값을 저장

    # key-value 아이디 - 신고자들(set)
    db_log = dict()
    db_banRequest = dict()
    # set 길이가 k 이상이면 - 정지당한유저다
    for key in id_list:
        db_log[key] = set()
        db_banRequest[key] = set()
    for r in report:
        a, b = r.split(" ")
        db_banRequest[a].add(b)
        db_log[b].add(a)
    print("db_log", db_log)
    print("db_banRequest", db_banRequest)
    # 밴요청 리퀘스트 보면서, 알림 주기

    for key, value in db_banRequest.items():
        ans = 0
        for target in value:
            if len(db_log[target]) >= k:
                ans += 1
        answer.append(ans)
    return answer


print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "muzi frodo", "muzi frodo", "apeach frodo",
        "frodo neo", "muzi neo", "apeach muzi"], 2
))
