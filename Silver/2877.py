import sys


def input(): return sys.stdin.readline().rstrip()


k = int(input())

a = 0
b = 0
idx = 0
for i in range(1, 2**20):
    a = b
    b += 2**i
    if a < k and k <= b:
        idx = i
        #print(a, b, idx)
        break
# i자리수의 , howsh 이진수
howsh = k - (a+1)
# print(howsh)
howsh = bin(howsh)[2:]
su = howsh.rjust(idx, "0")
su = su.replace("0", "4")
su = su.replace("1", "7")
print(su)
