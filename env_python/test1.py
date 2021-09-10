#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'smallestNegativeBalance' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY debts as parameter.
#

def smallestNegativeBalance(debts):
    data = dict()
    # 데이터에는 , 돈을 주는 사람 - , 돈을 받는 사람 + , 돈
    # (기억 안남 - 잔고인지 ... +1000, -1000)
    for debt in debts:
        # A,B,돈 - A는 돈만큼 감소, B는 돈만큼 증가
        # 이를 debts를 순회하면서, dict 데이터를 업데이트
        NName, PName, money = debt
        money = int(money)
        if NName in data:
            data[NName] -= money
        else:
            data[NName] = -money
        if PName in data:
            data[PName] += money
        else:
            data[PName] = money
    # 결과 값 (잔액) 중 음수를 정렬해서 리스트로 반환
    values = data.values()
    values = sorted(list(filter(lambda v: v < 0, values)))
    # 음수값이 없다면 Nobody .. 메시지를 출력
    if len(values) == 0:
        return ["Nobody has a negative balance"]
    targetM = values[-1]
    # print(values, targetM)
    # 그렇지 않다면, 가장 큰 음수값을 구해서
    # 그 음수 값을 가진 사람의 이름(key)값을 찾아서 리턴
    ans = []
    for key in data.keys():
        if data[key] == targetM:
            ans.append(key)
    ans.sort()
    print(data)
    return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('./output.txt', 'w')
    debts_rows = int(input().strip())
    debts_columns = int(input().strip())

    debts = []

    for _ in range(debts_rows):
        debts.append(input().rstrip().split())

    result = smallestNegativeBalance(debts)
    print(result)
    exit(0)
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

"""
5
3
Alex Blake 5
Blake Alex 3
Casey Alex 7
Casey Alex 4
Casey Alex 2
>['Casey']

5
3
Alex Blake 5
Blake Alex 3
Casey Alex 7
Casey Alex 4
Casey Alex 2
>['Casey']

6
3
a b 2
b a 2
c a 5
b c 7
a b 4
a c 4
>[a,b]

5
3
a b 10
a b 10
a b 10
a b 10
a b 10
>[a]

4
3
a b 10
b a 10
b a 10
a b 10
>['Nobody has a negative balance']


4
3
a b 10
b c 10
c d 10
d a 10
>['Nobody has a negative balance']
"""
