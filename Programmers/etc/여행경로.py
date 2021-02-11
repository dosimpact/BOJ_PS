

import sys
from copy import deepcopy

sys.setrecursionlimit(10**8)

Tickets = []
ans = []


def DFS(now: str, checkT: [], log: []):
    global ans

    if len(log) == len(Tickets)+1:
        res = deepcopy(log)
        ans.append(res)
        return

    for idx, [u, v] in enumerate(Tickets):
        if u == now and checkT[idx] == False:
            log.append(v)
            checkT[idx] = True
           # print(f" go {u} > {v}")
            DFS(v, checkT, log)
            checkT[idx] = False
            log.pop()


def solution(tickets):
    global Tickets
    Tickets = sorted(tickets)
    checkT = [False]*(len(tickets))
    log = []
    log.append("ICN")

    DFS("ICN", checkT, log)

    ans.sort()
    return ans[0]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
      "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
