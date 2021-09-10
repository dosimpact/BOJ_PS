data = [1, 3, 5, 7, 9]
query = 10

start, end = 0, len(data)
while start != end:
    if query <= data[(start + end) // 2]:
        end = (start + end) // 2
    elif data[(start + end) // 2] < query:
        start = (start + end) // 2 + 1

print(start, "[ idx ] query : ", query)

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
    # Write your code here
    return [1, 2, 3]


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("./output.txt", "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    # print('\n'.join(map(str, result)))
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
