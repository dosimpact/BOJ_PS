# 출력 진수 포멧 정하기
# https://www.acmicpc.net/problem/11816
a = input()
if(a[0] == '0'):
    if(a[0:2] == '0x'):
        print(int(a[2:], 16))
    else:
        print(int(a[1:], 8))

else:
    print(int(a))
