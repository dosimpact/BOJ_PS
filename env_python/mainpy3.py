from itertools import combinations


def solution(infos, qureies):
    answer = []
    db = dict()  # 4가지요소를 /으로 연결
    for info in infos:
        profiles = [i for i in info.split(" ")]
        score = int(profiles[-1])
        profiles = profiles[:-1]
        for i in range(5):  # 1개를 - 처리하는 경우 (~ 4개를)
            # 4개의 정보중 가릴 1개를 찾는 리스트
            pickCases = list(combinations(range(4), i))
            # pickCases - 1개만 - 을 치는 경우
            for idxs in pickCases:  # (1,2,3) < []
                profilesCopy = profiles.copy()
                for idx in idxs:
                    profilesCopy[idx] = "-"
                key = "|".join(profilesCopy)
                if key in db:
                    db[key].append(score)
                else:
                    db[key] = [score]
    for key in db:
        db[key].sort()
    for query in qureies:
        keys = [i for i in query.split(" ") if i != "and"]
        score = int(keys[-1])
        queryKey = "|".join(keys[:-1])
        if queryKey in db:
            scores = db[queryKey]  # scores 이분탐색 하여 , query 이상의 idx를 찾아내자.
            start, end = 0, len(scores)
            while start != end and start != len(scores):
                if scores[(start+end)//2] >= score:
                    end = (start+end)//2
                else:
                    start = (start+end)//2 + 1
            print(len(scores) - start)
            answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer


print(solution(
    ["java backend junior pizza 150",
     "python frontend senior chicken 210",
     "python frontend senior chicken 150",
     "cpp backend senior pizza 260",
     "java backend junior chicken 80",
     "python backend senior chicken 50"],

    ["java and backend and junior and pizza 100",
     "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250",
     "- and backend and senior and - 150",
     "- and - and - and chicken 100",
     "- and - and - and - 150"]
))
