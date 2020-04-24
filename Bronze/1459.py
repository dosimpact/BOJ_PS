

import sys


def input(): return sys.stdin.readline().rstrip()


x, y, w, s = map(int, input().split())

if 2*w <= s:  # w가 무조건 개이득
    print((x+y)*w)
# elif w > s:
#     mc = min(x, y)
#     more = max(x-mc, y-mc)
#     print(mc*s + more*w)
elif w > s:  # 대각선 스택이 압도적으로 개이득
    if (x+y) % 2 == 0:
        print(max(x, y)*s)
    else:
        print((max(x, y)-1)*s + w)
# elif 2*w < s and s >= w:
else:  # 섞어서 써야하는 경우
    mc = min(x, y)
    more = max(x-mc, y-mc)
    print(mc*s + more*w)
"""
fb) 

하나의 블럭에서
대각선으로 가는경우, 직선으로 두번 가능경우 > 
대각선을 가는 경우가 이득이라면, 최대한 대각선으로 가고, 최대한 이득을 본다음에 ( 틀림 ) 직선으로 간다.

집까지 가는데 더 이득을 볼 수 있다.
대각선으로 만 가는경우


"""
