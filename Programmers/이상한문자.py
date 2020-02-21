
import sys


def input(): return sys.stdin.readline().rstrip()

# dp 로 풀자 , topdown | d[k] 는 k까지 도달하는데 최소 전기량 | d[k] = min(d[k/2],d[k/4]...) 이게 넘사벽 <- or min ( d[k-1] + 1, d[k-2] +2, ... d[0] + k) 다 해봐야됨


def solution(s):
    ans = []
    dl = s.split()
    print(dl)
    for e in dl:
        d = list(e)
        tmp = ""
        for i in range(len(d)):
            if i % 2 == 0:
                tmp += str.upper(d[i])
            else:
                tmp += str.lower(d[i])
        ans.append(tmp)
    return " ".join(map(lambda e: "".join([a.lower() if i % 2 == 0 else a.upper() for (i, a) in enumerate(e)]), s.split(" ")))


print(solution("___try hello world strys___"))


"""
+k) str.upper, str.lower
문자 대소문자 변경하기

FB) splite에 문제가 있었음 아직도 잘 모르겠지만, splite를 바꿔보는것도 하나의 방법
splite() vs splite("")

"""
