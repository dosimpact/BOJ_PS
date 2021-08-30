# 1초
print(1*1000)  # 1000 ms
# 1분 = 60초
print(1*60*1000)  # 60,000 ms
# 1시간 = 60분
print(1*60*60*1000)  # 3,600,000 ms
# 1일 = 24시
print(1*24*60*60*1000)  # 86,400,000 ms


def toIOSTime(su):
    "15:01:00.001"
    year, su = divmod(su, (12*30*24*60*60*1000))  # ❌ 윤년
    month, su = divmod(su, (30*24*60*60*1000))  # ❌ 28,30,31
    day, su = divmod(su, (24*60*60*1000))

    h, su = divmod(su, (60*60*1000))
    m, su = divmod(su, (60*1000))
    s, su = divmod(su, (1000))
    ms = su
    return f"{year}-{month}-{day} {h}:{m}:{s}.{ms}"


print(toIOSTime(1630029532619))
