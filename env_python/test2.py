#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'smallestNegativeBalance' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY debts as parameter.

def taxiDriver(pickup, drop, tip):
    print(pickup, drop, tip)
    iList = [[pickup[i], drop[i], tip[i]] for i in range(len(pickup))]
    iList.sort(key=lambda x: (x[0]))
    memo = defaultdict(int)
    M = 0  # last max pickup earning
    # [11, 30, 0, 21, 41, 19] [20, 31, 17, 22, 46, 21] [6, 1, 9, 0, 8, 0]
    for idx, (pickPtn, dropPtn, tip) in enumerate(iList):
        logs = list(map(lambda key: memo[key], list(
            filter(lambda x: x <= pickPtn, memo.keys()))))
        if logs:
            M = max(logs)
        memo[dropPtn] = max(M + tip+(dropPtn - pickPtn), memo[dropPtn])
    return max(memo.values())


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

"""
2
1
4
2
5
6
2
2
5

3
0
4
5
3
3
5
7
3
1
2
2

6
11
30
0
21
41
19
6
20
31
17
22
46
21
6
6
1
9
0
8
0
>55 ❌
>44 ✅
"""
