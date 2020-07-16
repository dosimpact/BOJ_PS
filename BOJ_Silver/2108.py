import sys
from collections import defaultdict
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


d_dict = {}
N = int(input())
datas = []
for _ in range(N):
    d = int(input())
    datas.append(d)
    if d in d_dict:
        d_dict[d] += 1
    else:
        d_dict[d] = 1


datas.sort()
# print(datas)
print(round(sum(datas) / len(datas)))
print(datas[len(datas) // 2])


maxCnt = max(d_dict.values())
result = []
for key in d_dict:
    if d_dict[key] == maxCnt:
        result.append(key)
result.sort()
if len(result) == 1:
    print(result[0])
else:
    print(result[1])


print(max(datas) - min(datas))


"""
FB) 1.  문제를 제대로 안읽는 습관 
- N이 홀수라는 가정을 안보고, 엄청난 손해를 봤다.

FB) 끝점 TDD 안하려는 ㅅㅂ관


FB) 2. 문제를 제대로 안읽는 습관
- 최빈값에서 ,여러개일경우  2번째출력을 안봤다.
- 산술평균 출력할때, 소수첫째자리에서 반올림을 하면, round(su,1) 이 아니라, round(su) 이다.

"""

