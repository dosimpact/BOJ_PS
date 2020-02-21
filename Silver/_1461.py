
import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
print(N, M)

books = sorted(list(map(int, input().split())), reverse=True)
didbs = list(filter(lambda x: x > 0, books))
dmabs = sorted(
    list(map(lambda x: abs(x), filter(lambda x: x < 0, books))), reverse=True)

ans = 0


def popbook(book, w):
    global ans
    ans += max(book)*w
    book.pop(0)
    if len(book) != 0:
        book.pop(0)


# 양북만 있는 경우 | 음북만 있는 경우 | 둘다 있는 경우
if len(didbs) != 0 and len(dmabs) == 0:
    popbook(didbs, 1)
    while(len(didbs) != 0):
        popbook(didbs, 2)

elif len(didbs) == 0 and len(dmabs) != 0:
    popbook(dmabs, 1)
    while(len(dmabs) != 0):
        popbook(dmabs, 2)

elif len(didbs) != 0 and len(dmabs) != 0 and max(didbs) >= max(dmabs):
    popbook(didbs, 1)
    while(len(didbs) != 0):
        popbook(didbs, 2)
    while(len(dmabs) != 0):
        popbook(dmabs, 2)

elif len(didbs) != 0 and len(dmabs) != 0 and max(didbs) < max(dmabs):
    popbook(dmabs, 1)
    while(len(didbs) != 0):
        popbook(didbs, 2)
    while(len(dmabs) != 0):
        popbook(dmabs, 2)

print(ans)
"""
그리디 알고리즘 : 역으로 생각해서, 접근!

1.무조건 책을 한번에 많이 가져다 두는게 이득
2. 제일 먼 거리 책은 마지막에 하는게 이득

"""
