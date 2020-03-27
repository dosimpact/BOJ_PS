
N = 5
"""
3
YZZ
ZYZ
ZZY
[['Y', 'C', 'P', 'Z', 'Y'], 
['C', 'Y', 'Z', 'Z', 'P'], 
['C', 'C', 'P', 'P', 'P'], 
['C', 'Y', 'Y', 'Z', 'C'], 
['C', 'P', 'P', 'Z', 'Z']]
"""


def maxVal():
    graph = [['Y', 'C', 'P', 'Z', 'Y'], ['C', 'Y', 'Z', 'Z', 'P'], [
        'C', 'C', 'P', 'P', 'P'], ['C', 'Y', 'Y', 'Z', 'C'], ['C', 'P', 'P', 'Z', 'Z']]
    ans = 0
    # 가장 긴 연속 부분(행 또는 열)을
    for i in range(N):
        tmp = 1
        for j in range(N-1):  # 0 1 2 3      [][][][][]
            if graph[i][j] == graph[i][j+1]:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1
            print("->", graph[i][j], graph[i][j+1], "->", ans)

    print(ans)
    for j in range(N):  # 0
        tmp = 1
        for i in range(N-1):  # 0 1 2 3
            if graph[i][j] == graph[i+1][j]:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1
        ans = max(ans, tmp)
    print(ans)
    return ans


maxVal()
