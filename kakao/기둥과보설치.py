def check(ans):
    for x, y, a in ans:
        # 0:기둥 1:보
        if a == 0:
            if y == 0 or [x, y-1, 0] in ans:
                continue
            if [x-1, y, 1] in ans or [x, y, 1] in ans:
                continue
            else:
                return False
        elif a == 1:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans:
                continue
            if [x-1, y, 1] in ans and [x+1, y, 1] in ans:
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    ans = []
    for i in build_frame:
        x, y, a, b = i
        # 0:삭제 1:설치
        if b == 1:
            ans.append([x, y, a])
            if check(ans) == True:
                continue
            else:
                ans.remove([x, y, a])
        if b == 0:
            if [x, y, a] in ans:
                ans.remove([x, y, a])
                if check(ans):
                    continue
                else:
                    ans.append([x, y, a])
    ans.sort()
    return ans


"""


"""
