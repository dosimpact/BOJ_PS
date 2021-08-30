
Memo = dict()


def dp(n: int):
    Memo['a'] = 0
    while True:
        isBreak = True
        for key in Memo.keys():
            if Memo[key] == 0:
                isBreak = False
                Memo[key] = 1
                aCnt = key.count("a")
                print(f"key :{key} aCnt {aCnt}")
                for nxt in ["b"*aCnt + key + "b"*aCnt, key + "a", "a" + key]:
                    if len(nxt) > n:
                        continue
                    Memo[nxt] = 0
        if isBreak:
            break


def solution(a):
    answer = []
    dp(max(list(map(lambda x: len(x), a))))
    print(Memo)
    return None


print(solution(["abab", "bbaa", "bababa", "bbbabababbbaa"]))
# RuntimeError: dictionary changed size during iteration
