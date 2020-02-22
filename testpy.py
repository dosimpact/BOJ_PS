import sys


def input(): return sys.stdin.readline().rstrip()


"""
명령어 + 인덱서
데이터(0~255) + 포인터(0~32766)
"""
PTR_RANGE = 32767

T = int(input())
for i in range(1, T+1):
    print('PROGRAM #%d:' % i)

    indexer = 0
    cmd = ""

    data = [0 for _ in range(PTR_RANGE)]
    ptr = 0

    while(True):
        lin = "".join(list(input().split(" ")))
        if 'end' in lin:
            break
        if '%' in lin:
            cmd += lin[:lin.index('%')]
            continue
        cmd += lin

    # print(cmd)
    # print(len(cmd))

    if cmd.count('[') != cmd.count(']'):
        print('COMPILE ERROR')
    else:
        while(True):
            # print('DEBUG:', data[0:2], 'ptr : ', ptr, 'indexer', indexer)
            # 현재 인덱서의 cmd를 실행시킨다.
            if cmd[indexer] == '+':
                data[ptr] = data[ptr]+1 if (data[ptr]+1 <= 255) else 0
                indexer += 1
            elif cmd[indexer] == '-':
                data[ptr] = data[ptr]-1 if (data[ptr]-1 >= 0) else 255
                indexer += 1
            elif cmd[indexer] == '>':
                ptr = (ptr + 1) if (ptr + 1) < PTR_RANGE else 0
                indexer += 1
            elif cmd[indexer] == '<':
                ptr = (ptr - 1) if (ptr - 1) >= 0 else PTR_RANGE-1  # ?????
                indexer += 1
            elif cmd[indexer] == '.':
                print(chr(data[ptr]), end='')
                indexer += 1
            elif cmd[indexer] == '[':
                if data[ptr] == 0:
                    indexer = indexer + cmd[indexer::1].index(']')
                else:
                    indexer += 1
            elif cmd[indexer] == ']':
                if data[ptr] != 0:
                    indexer = indexer - cmd[indexer::-1].index('[')
                else:
                    indexer += 1
            # 현재 인덱서를 하나 증가시키고 | 만약 끝이라면
            if indexer == len(cmd):
                break
        print()
"""
fb)
data = [1, 2, 3, 4, 5, 6, 7]
print(data[1:4])  # [2, 3, 4]
print(data[4:1:-1])  # [5, 4, 3]

print(data[::].index(3))  # 앞에서 3은 2번인덱스
print(data[::-1].index(3))  # 뒤에서 3은 1번 인덱스


++++++++++++++++++++++++++>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++<[>.+<-]

"""
