#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):
    data = list(set(ranked))
    data = list(map(lambda x: -x, data))
    player = list(map(lambda x: -x, player))
    data.sort()
    ans = []
    print(player, data)
    for query in player:
        start, end = 0, len(data)
        while start != end:
            if query <= data[(start + end) // 2]:
                end = (start + end) // 2
            else:
                start = (start + end) // 2 + 1
        if start == len(data):
            ans.append(start + 1)
            data.append(query)
        elif query == data[start]:
            ans.append(start + 1)
        elif query != data[start]:
            ans.append(start + 1)
            data.insert(start, query)
        print("data", data, "start", start)
    print(ans)
    return ans


"""
10
100 101 102 103 104 105 106 107 108 109
10
0 0 0 0 0 0 0 0 0 0 
"""

if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    fptr = open("output.txt", "w")
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()


def solution(infos, qureies):
    answer = []
    db = [dict() for i in range(len(infos))]
    for idx, info in enumerate(infos):
        lang, part, level, food, score = info.split(" ")
        db[idx]["lang"] = lang
        db[idx]["part"] = part
        db[idx]["level"] = level
        db[idx]["food"] = food
        db[idx]["score"] = score

    for query in qureies:
        qListTmp = query.split(" ")
        qList = [qListTmp[0], qListTmp[2], qListTmp[4], qListTmp[6], qListTmp[7]]
        filtered = list(
            filter(
                lambda x: (
                    int(x["score"]) >= int(qList[4]) if qList[4] != "-" else True
                )
                and (x["part"] == qList[1] if qList[1] != "-" else True)
                and (x["level"] == qList[2] if qList[2] != "-" else True)
                and (x["food"] == qList[3] if qList[3] != "-" else True)
                and (x["lang"] == qList[0] if qList[0] != "-" else True),
                db,
            )
        )
        answer.append(len(filtered))
    return answer


print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)

