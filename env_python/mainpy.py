def cutNumber(num, su):
    return ((num//su)*su)


def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"": 1, "*": 2, "#": -1}

    p = re.compile("(\d+)([SDT])([*#]?)")

    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == "*" and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]


def solution(money, minratio, maxratio, ranksize, threshold, months):
    prints = []
    for _ in range(months):
        # 소유 가정 금액
        cuttedMoney = cutNumber(money, 100)
        p = getPercentage(cuttedMoney, threshold, ranksize, minratio, maxratio)
        prints.append((money, p))
        money = money - cuttedMoney*(p*0.01)
    # print(prints)
    return money
