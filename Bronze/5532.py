
import sys
import math
import functools
import itertools

DEBUG = False


def input(): return sys.stdin.readline().rstrip()


L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

ko = divmod(A, C)
en = divmod(B, D)

taskdays = 0
taskdays = max(en[0] if en[1] == 0 else en[0]+1,
               ko[0] if ko[1] == 0 else ko[0]+1)
print(L - taskdays)
