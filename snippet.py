"""

"""


import sys
t = [7, 2, 3, 6, 5, 4, 1]

res = sys.stdin.read()
res = list(map(int, res.split()))


while len(res) != 0:
    a = res.pop(0)
    b = res.pop(0)
    if a == -1:
        break
    print("a,b", a, b)
