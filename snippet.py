
# XX..A..CCC...BBB


def isVaild(s: []):
    cnt = 0
    now = "."
    # .인경우는 무조건 초기화
    for i in range(len(s)):
        # .이 아닌 경우, 같은거 또 나온겨우
        if s[i] == '.':
            cnt = 0
            now = '.'
        else:
            if now == s[i]:
                cnt += 1
                if cnt >= 3:
                    return now
            else:
                now = s[i]
                cnt = 1

                # 다른게 나온경우. ( . 에서 새롭게 나온경우)
    return '.'


print(isVaild("KKYK.....XX..A..CCBC...BB.TTT"))
