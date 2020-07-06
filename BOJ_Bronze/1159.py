"""
https://www.acmicpc.net/problem/1159

성의 첫 글자가 같은 선수 5명을 선발

성의 첫 글자가 같은 선수가 5명보다 적다면, 상근이는 내일 있을 친선 경기를 기권

"""
import sys
def input(): return sys.stdin.readline().rstrip()
# 입력


N = int(input())
check = [0]*26

for _ in range(N):
    name = input()
    check[ord(name[0])-ord('a')] += 1

how = []
for i, c in enumerate(check):
    if c >= 5:
        how.append(chr(ord('a')+i))
# 첫글자만 check에 카운팅
if how:
    how.sort()
    for h in how:
        print(h, end="")
    pass
else:
    print("PREDAJA")
# 5가 되는것들 사전순 출력


# 없으면 항복
