def cutNumber(num, su):
    return ((num//su)*su)


​


def getPercentage(m, threshold, ranksize, minratio, maxratio):
    if m < threshold:
        return 0
    step = 0
    while True:
        if minratio + step >= maxratio:
            return maxratio
        # 범위 체크
        if threshold + ranksize*step <= m < threshold + ranksize*(step+1):
            return minratio + step
        step += 1


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
