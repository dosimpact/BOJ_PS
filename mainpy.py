
import sys


def input(): return sys.stdin.readline().rstrip()


(A, B, C) = map(int, input().split())
print((A+B) % C)
print((A % C + B % C) % C)
print((A*B) % C)
print((A % C * B % C) % C)
