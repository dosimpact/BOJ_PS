import sys
input = sys.stdin.readline


sens = input().strip()
data = []

while sens:
    # 태그인 경우 - 태그까 끝날떄까지 반복
    if sens[0] == "<":
        tmp = sens[0]
        sens = sens[1:]
        while sens[0] != ">":
            tmp += sens[0]
            sens = sens[1:]
        tmp += sens[0]
        sens = sens[1:]
        data.append(tmp)

    elif sens[0] == " ":
        data.append(" ")
        sens = sens[1:]
    else:  # 단어인경우 - " " 나올때까지 단어 더하기
        tmp = sens[0]
        sens = sens[1:]
        while sens and (sens[0] != " " and sens[0] != "<"):  # 💥FB
            # while sens and sens[0] != " " and sens[0] != "<":  # 💥FB
            tmp += sens[0]
            sens = sens[1:]
        data.append(tmp[::-1])
print("".join(data))
