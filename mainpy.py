
import sys


def input(): return sys.stdin.readline().rstrip()

# dp 로 풀자 , topdown | d[k] 는 k까지 도달하는데 최소 전기량 | d[k] = min(d[k/2],d[k/4]...) 이게 넘사벽 <- or min ( d[k-1] + 1, d[k-2] +2, ... d[0] + k) 다 해봐야됨


data = '12ST'
print(data)
for e in data:
    if e >= '1' and e <= '9':
        print(int(e)**2)
