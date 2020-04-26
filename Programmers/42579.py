

import sys


def input(): return sys.stdin.readline().rstrip()


Debug = True


def solution(genres, plays):
    ans = []
    data = {}
    metaData = {}
    for idx, (gen, playtime) in enumerate(zip(genres, plays)):
        # print(gen, playtime)
        if gen not in data:
            data[gen] = [(idx, playtime)]
            metaData[gen] = playtime
        else:
            data[gen].append((idx, playtime))
            metaData[gen] += playtime

    rank = []
    for key in metaData:
        rank.append((metaData[key], key))
    rank.sort(reverse=True)
    print(rank)
    for r in rank:
        nowPlayList = data[r[1]]
        nowPlayList.sort(key=lambda e: (-e[1], e[0]))
        if len(nowPlayList) == 1:
            ans.append(nowPlayList[0][0])
        else:
            ans.append(nowPlayList[0][0])
            ans.append(nowPlayList[1][0])
        # print(nowPlayList)
    return ans


print(solution(	["classic", "pop", "classic",
                 "classic", "pop"], [500, 600, 150, 800, 2500]))


"""
베스트 앨범

그냥 obj 다루는 문제임.
문제 조건대로 잘 풀면 됨ㄴ

"""
