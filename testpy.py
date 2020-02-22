import sys


def input(): return sys.stdin.readline().rstrip()


data = ['[', '1', '2', '3', '[', '5', ']']

print(data[::])

print(4+data[4::1].index(']'))
print(6 - data[6::-1].index('['))
