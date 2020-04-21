

import sys

Debug = False
DB = [
    [1967, "DavidBowie"],
    [1969, "SpaceOddity"],
    [1970, "TheManWhoSoldTheWorld"],
    [1971, "HunkyDory"],
    [1972, "TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars"],
    [1973, "AladdinSane"],
    [1973, "PinUps"],
    [1974, "DiamondDogs"],
    [1975, "YoungAmericans"],
    [1976, "StationToStation"],
    [1977, "Low"],
    [1977, "Heroes"],
    [1979, "Lodger"],
    [1980, "ScaryMonstersAndSuperCreeps"],
    [1983, "LetsDance"],
    [1984, "Tonight"],
    [1987, "NeverLetMeDown"],
    [1993, "BlackTieWhiteNoise"],
    [1995, "1.Outside"],
    [1997, "Earthling"],
    [1999, "Hours"],
    [2002, "Heathen"],
    [2003, "Reality"],
    [2013, "TheNextDay"],
    [2016, "BlackStar"],
]


def input(): return sys.stdin.readline().rstrip()


n = int(input())


def Query(s: int, e: int):
    res = []
    for row in DB:
        if s <= row[0] and row[0] <= e:
            res.append(row)
    return res


for _ in range(n):
    startYear, endYear = map(int, input().split())
    res = Query(startYear, endYear)
    print(len(res))
    for r in res:
        print(*r)
