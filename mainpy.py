
import sys


def input(): return sys.stdin.readline().rstrip()

# dp 로 풀자 , topdown | d[k] 는 k까지 도달하는데 최소 전기량 | d[k] = min(d[k/2],d[k/4]...) 이게 넘사벽 <- or min ( d[k-1] + 1, d[k-2] +2, ... d[0] + k) 다 해봐야됨


d = {0: 0, 1: 1, 2: 1, 500000: 7, 250000: 7, 125000: 7, 62500: 7, 31250: 7, 15625: 7, 15624: 6, 7812: 6, 3906: 6, 1953: 6, 1952: 5, 976: 5, 488: 5, 244: 5, 122: 5, 61: 5, 60: 4, 30: 4, 15: 4, 14: 3, 7: 3, 6: 2, 3: 2, 1000000000: 13, 500000000: 13, 250000000: 13, 125000000: 13, 62500000: 13, 31250000: 13, 15625000: 13, 7812500: 13, 3906250: 13, 1953125: 13, 1953124: 12, 976562: 12, 488281: 12, 488280: 11, 244140:
     11, 122070: 11, 61035: 11, 61034: 10, 30517: 10, 30516: 9, 15258: 9, 7629: 9, 7628: 8, 3814: 8, 1907: 8, 1906: 7, 953: 7, 952: 6, 476: 6, 238: 6, 119: 6, 118: 5, 59: 5, 58: 4, 29: 4, 28: 3}


def dp(n):
    if n in d:
        return d[n]
    else:
        d[n] = -1
        tmpn = n
        while(True):
            if tmpn % 2 == 0:
                tmpn = int(tmpn / 2)  # FB 파이썬에서 나누면 float가 된다. int로
                if d[n] == -1 or d[n] > int(dp(tmpn)):
                    d[n] = int(dp(tmpn))
                if tmpn == 0:
                    break
            else:
                break

        if d[n] != -1:
            pass
        else:
            d[n] = dp(n-1)+1
            # dlist = []
            # for e in range(n):
            #     dlist.append(dp(e) + (n-e))
            # d[n] = int(min(dlist))
        return d[n]


def solution(n):
    ans = dp(n)
    print(ans)
    print(d)
    return ans


solution(1000000000)
