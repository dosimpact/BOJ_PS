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
    # 입력 데이터는 픽업위치 배열, 드랍위치 배열, Tip 배열
    # 자료구조는 메모를 위해 defaultdict을 사용 , 그리고 M 이라는 임시 변수를 사용함
    print(pickup, drop, tip)
    iList = [[pickup[i], drop[i], tip[i]] for i in range(len(pickup))]
    print(iList)
    # 픽업위치순으로 정렬을 우선 먼저 한다. 순차적으로 DP를 하기 위함
    iList.sort(key=lambda x: (x[0]))
    print(iList)
    memo = defaultdict(int)
    M = 0  # last max pickup earning
    # [11, 30, 0, 21, 41, 19] [20, 31, 17, 22, 46, 21] [6, 1, 9, 0, 8, 0]

    # memo[n]의 정의 : 위치 n에서 벌 수 있는 최대 금액
    # memo[n]의 관계식 :
    # memo[n] = max ( memo[n] , 픽업위치일때 벌었던 최대 금액 + 이번 승객을 통해 번 돈  )
    # 이해하기 1. memo[n] = max(  이번 승객을 통해 번 돈 ,memo[n] )
    # 이해하기 2. memo[n] = max(  픽업위치일때 벌었던 최대 금액 + 이번 승객을 통해 번 돈  )
    # 1+2 를 통해 위 결론식이 나옴
    for idx, pickPoint in enumerate(iList[0]):
        # input()
        # print(f"{idx}번째, pickPoint{pickPoint} 입니다.")
        logs = list(map(lambda key: memo[key], list(
            filter(lambda x: x <= pickPoint, memo.keys()))))
        # print(f"logs {logs}")
        if logs:
            M = max(logs)
        memo[iList[1][idx]] = max(M + iList[2][idx]+(iList[1][idx] -
                                                     iList[0][idx]), memo[iList[1][idx]])
    print(memo)
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
