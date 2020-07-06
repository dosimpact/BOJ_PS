"""
x사

"""


import sys


def input(): return sys.stdin.readline().rstrip()


xL = int(input())
yB = int(input())
ylimit = int(input())
yAdder = int(input())
p = int(input())

xprice = p*xL

yprice = yB
if p <= ylimit:
    pass
else:
    yprice += (p-ylimit)*yAdder
print(min([xprice, yprice]))
