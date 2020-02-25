import sys


def input(): return sys.stdin.readline().rstrip()


def isRight(cd):
    st = 0
    for i in range(0, len(cd)):
        if cd[i] == '[':
            st += 1
        elif cd[i] == ']':
            st -= 1
            if st < 0:
                return False
    if st == 0:
        return True
    else:
        return False


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

    if not isRight(cmd):  # fb) 올바른 괄호인지도 판단;;
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
                ptr = 0 if (ptr == PTR_RANGE) else ptr + 1
                indexer += 1
            elif cmd[indexer] == '<':
                ptr = PTR_RANGE if (ptr == 0) else ptr - 1
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

ptr = 0
arr = [0] * 32768
code = ''
res = []
index_map = dict()


def parse(idx):
    global ptr, arr, code, index_map
    ch = code[idx]

    if ch == '>':
        ptr = 0 if ptr == 32767 else ptr + 1
    elif ch == '<':
        ptr = 32767 if ptr == 0 else ptr - 1
    elif ch == '+':
        arr[ptr] = 0 if arr[ptr] == 255 else arr[ptr] + 1
    elif ch == '-':
        arr[ptr] = 255 if arr[ptr] == 0 else arr[ptr] - 1
    elif ch == '.':
        res.append(chr(arr[ptr]))
    elif ch == '[':
        return index_map[idx] + 1 if arr[ptr] == 0 else idx + 1
    elif ch == ']':
        return index_map[idx] if arr[ptr] != 0 else idx + 1

    return idx + 1


def main():
    global ptr, arr, code, index_map, res

    n = int(input())
    for i in range(1, n + 1):
        ptr = 0
        index_map.clear()
        arr = [0] * 32768
        res.append("PROGRAM #%d:\n" % i)

        buf = []

        while True:
            line = input().replace(" ", "")
            if 'end' == line:
                break

            buf.append(line[:line.find('%')] if '%' in line else line)

        code = ''.join(buf)
        stk = []

        for j in range(0, len(code)):
            ch = code[j]
            if ch == '[':
                stk.append(j)
            elif ch == ']':
                idx = stk.pop()
                index_map[j] = idx
                index_map[idx] = j

        if len(stk) == 0:
            j = 0
            while j < len(code):
                j = parse(j)
        else:
            res.append('COMPILE ERROR')
        res.append('\n')

    print(''.join(res))


main()
"""
