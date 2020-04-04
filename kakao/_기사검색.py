
import sys

# 쿼리에 대한 전체 결과다.
memo = {}
# 특정 단어와 쿼리에 대한 결과 메모
memoWQ = {}
# 단어의 길이들을 저장한다. 예 ) 단어 길이가 2인 것의 갯수는 5개 이다.
memoWL = {}


def CheckHead(word: str, q: str):  # ? 가 앞대가리
    i = len(word) - 1
    isposs = True
    while 0 < i:
        if q[i] == '?':
            break
        else:
            if q[i] == word[i]:
                pass
            else:
                isposs = False
                break
        i -= 1
    return isposs


def CheckTail(word: str, q: str):  # ? 가 뒤에
    i = 0
    isposs = True
    while i < len(word):
        if q[i] == '?':
            break
        else:
            if q[i] == word[i]:
                pass
            else:
                isposs = False
                break
        i += 1
    return isposs


def Result(words: [], q: str):

    if q in memo:
        return memo[q]

    L = len(q)
    # q가 다 ? 인경우
    if len(q) == q.count('?'):
        if L in memoWL:
            return memoWL[L]
        return 0
        # res = 0
        # for word in words:
        #     if len(word) == L:
        #         res += 1
        # return res
    # ? 접두
    if q[0] == '?':
        res = 0
        for word in words:
         # 우선 길이가 맞아야 한다.
            if len(word) != L:
                continue
            else:  # 길이가 맞다면 q에서 뒤에서 검색을 하면서, ?가 나올때 까지, 일치하는지 검사.
                if CheckHead(word, q):
                    res += 1
    # ? 접미
    if q[-1] == '?':
        res = 0
        for word in words:
         # 우선 길이가 맞아야 한다.
            if len(word) != L:
                continue
            else:  # 길이가 맞다면 q에서 뒤에서 검색을 하면서, ?가 나올때 까지, 일치하는지 검사.
                if CheckTail(word, q):
                    res += 1
    memo[q] = res
    return res


def solution(words, queries):
    answer = []
    for word in words:
        tLen = len(word)
        if tLen in memoWL:
            memoWL[tLen] += 1
        else:
            memoWL[tLen] = 1

    for q in queries:
        answer.append(Result(words, q))
    return answer


"""

["frodo", "front", "frost", "frozen", "frame", "kakao"]	[
    "fro??", "????o", "fr???", "fro???", "pro?"]	[3, 2, 4, 1, 0]


문자열 검색시 사용하는 트라이 자료구조

"""
# print(CheckHead("kakoo", "??kao"))
# print(CheckTail("kakao", "kaka?"))
