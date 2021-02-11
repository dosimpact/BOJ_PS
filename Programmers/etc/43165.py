
import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()

# 현재 인덱스와, 현재까지의 합


Max_idx = 0  # len numbers
Target = 0
Ans = 0
Numbers = []


def go(idx, now):
    global Ans
    # 인덱스가 차면 체크후 되면 ++
    if idx == Max_idx:
        if now == Target:
            return 1
        return 0
    # 인덱스가 안찬경우 -> +,- 로 각각 재귀호출
    return go(idx+1, now+Numbers[idx])+go(idx+1, now-Numbers[idx])


def solution(numbers, target):
    global Max_idx, Target, Ans, Numbers
    Max_idx = len(numbers)
    Numbers = numbers
    Target = target
    return go(0, 0)


solution([1, 1, 1, 1, 1], 3)
print(Ans)


# def solution(numbers, target):
#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
