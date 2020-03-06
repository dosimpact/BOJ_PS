def solution(words):
    ans = ""
    counter = 0
    for i in range(len(words)):
        if words[i] == " ":
            counter = 0
            ans += " "
        else:
            if counter % 2 == 0:
                ans += words[i].upper()
            else:
                ans += words[i].lower()
            counter += 1
    return ans