

import sys


Debug = False

userList = {}
blackList = {}
products = None
parsedData = {}
User_id = None


def match(black: str, user: str):
    for i in range(len(black)):
        if black[i] == '*':
            continue
        if black[i] != user[i]:
            return False
    return True


def addparsedData(blackname: str, name: str):
    NL = len(blackname)
    if NL not in parsedData:
        parsedData[NL] = {}


def solution(user_id, banned_id):
    global userList, blackList, products, user_id
    User_id = user_id

    # ----
    for user in user_id:
        L = len(user)
        if L not in userList:
            userList[L] = [user]
        else:
            userList[L].append(user)

    for user in banned_id:
        L = len(user)
        if L not in blackList:
            blackList[L] = [user]
        else:
            blackList[L].append(user)
    products = [0] * len(userList.keys())
    if Debug:
        print(userList)
        print(blackList)
        print(products)

    for idx, nameLen in enumerate(blackList.keys()):
        blist = blackList[nameLen]
        ulist = userList[nameLen]
        for usera in blist:
            for userb in ulist:
                if match(usera, userb):
                    # products[idx] += 1
                    addparsedData(usera, userb)
    # if Debug:
    #     print(products)
    # res = 1
    # for p in products:
    #     res = res * p
    return res


print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], [
      "fr*d*", "*rodo", "******", "******"]))
