import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
for _ in range(n):
    num, su = input().split()
    octsu = ""
    hexsu = ""
    try:
        octsu = int("0o"+su, 8)
    except:
        octsu = "0"
    # fb)> 그대로 출력해서, 0001은 1로 출력해야하는데, 0001이 나와버림.!!!
    #print(num, octsu, su, int("0x"+su, 16))
    print(num, octsu, int(su, 10), int("0x"+su, 16))

"""
    # fb)> 그대로 출력해서, 0001은 1로 출력해야하는데, 0001이 나와버림.!!!
    #print(num, octsu, su, int("0x"+su, 16))
    print(num, octsu, int(su, 10), int("0x"+su, 16))

"""
