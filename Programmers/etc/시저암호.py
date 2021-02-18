
import sys


def input(): return sys.stdin.readline().rstrip()


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + n) % 26)
        elif s[i] >= 'A' and s[i] <= 'Z':
            s[i] = chr(ord('A') + (ord(s[i]) - ord('A') + n) % 26)
    return "".join(s)
