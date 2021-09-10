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

