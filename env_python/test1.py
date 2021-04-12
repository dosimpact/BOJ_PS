from sys import stdin, setrecursionlimit
from itertools import combinations
from collections import deque, defaultdict


seed = 1000000
label = ["주식1", "주식1", "채권1", "채권1", "금", "원자재1", "원자재2", "원자재3", "원자재4"]
ratio = [15, 15, 35, 20.5, 7.5, 1.75, 1.75, 1.75, 1.75]

print(f"--- Seed : {seed}(원) 일때 올웨더 분배 금액 ---")
for i in range(len(label)):
    print(f"{label[i]} : { seed *(ratio[i]/100) }")