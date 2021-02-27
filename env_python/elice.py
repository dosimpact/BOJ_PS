from math import ceil
import sys
from typing import *

input = sys.stdin.readline


# 폭탄 ( , 레이져 )

def main():
    S = input().strip()
    if S.count("(") == S.count(")"):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()


"""
(())()()
YES

))((
YES

))(()
NO
"""
