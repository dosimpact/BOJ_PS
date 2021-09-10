#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'taxiDriver' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY pickup
#  2. LONG_INTEGER_ARRAY drop
#  3. INTEGER_ARRAY tip
#

def taxiDriver(pickup, drop, tip):
    # Write your code here
    n = max(drop)
    dp = [0]*(n+1)
    M = 0  # last max pickup earning
    # lastPoint = 0
    print(pickup, drop, tip)  # [1, 4] [5, 6] [2, 5]
    for idx, pickPoint in enumerate(pickup):
        # lastPoint = pickPoint
        # M = max(M, dp[pickPoint])
        M = max(dp[:pickPoint+1])
        dp[drop[idx]] = max(M + tip[idx]+drop[idx]-pickup[idx], dp[drop[idx]])
    print(dp)
    return max(dp)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('./output.txt', 'w')
    pickup_count = int(input().strip())

    pickup = []

    for _ in range(pickup_count):
        pickup_item = int(input().strip())
        pickup.append(pickup_item)

    drop_count = int(input().strip())

    drop = []

    for _ in range(drop_count):
        drop_item = int(input().strip())
        drop.append(drop_item)

    tip_count = int(input().strip())

    tip = []

    for _ in range(tip_count):
        tip_item = int(input().strip())
        tip.append(tip_item)

    result = taxiDriver(pickup, drop, tip)
    print(result)
    exit(0)
    fptr.write(str(result) + '\n')
    fptr.close()
