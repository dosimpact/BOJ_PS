wordNum = input()
word = []
for i in range(int(wordNum)):
    temp = input()
    word.append(list(temp))
number = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# word: AAA AAB

charDic = {}
for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in charDic:
            charDic[word[i][j]] = pow(10, len(word[i])-j-1)
        else:
            charDic[word[i][j]] += pow(10, len(word[i])-j-1)

keyList = list(charDic.keys())
for i in range(len(keyList)-1):
    big = i
    for j in range(len(keyList)-i-1):
        if charDic[keyList[j]] < charDic[keyList[j+1]]:
            keyList[j], keyList[j+1] = keyList[j+1], keyList[j]

result = 0
for i in keyList:
    result += number.pop(0) * charDic[i]

print(result)
