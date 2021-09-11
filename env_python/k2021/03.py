import math
# 입차 출차 기록, 주차 욕므 계산
# 요금표 - 기본시간-기본요금-단위시간 + 단위요금
# 기본 시간
# 기본 요금
# 단위 시간
# 단위 요금

# 시간-번호-IN|OUT

# 1. 누적 주차시간을 구한다
# 34 + 300 = 334
# 기본요금 5000 (3시간) + 올려서 요금 받기


def convert(string: str):  # 시:분 -> 분
    h, m = string.split(":")
    return int(h)*60 + int(m)


def payment(fees, time):
    # [180 기본 시간 , 5000 기본 요금, 10, 600],
    # 기본 요금 + 추가 요금
    base = fees[1]  # 1번 인덱스, 기본 요금
    extra = 0
    # 0번 인덱스 기본 시간 , 2번 인덱스 단위 시간,
    if time - fees[0] > 0:
        extra = math.ceil((time - fees[0])/fees[2])*fees[3]
    # print("base + extra", base, extra)
    return base + extra


def solution(fees, records):
    db_car = dict()
    answer = []
    # key-value 차량 번호 - [총 주차 시간,최근 출차 시각]
    # 돌면서 레코드 처리
    for record in records:
        time, num, io = record.split(" ")
        time = convert(time)
        # 번호 처리
        if num not in db_car:
            db_car[num] = [0, None]
        # 들어오는경우 - 기록하기 , 나가는 경우 - 시간 더하기
        if io == "IN":
            db_car[num] = [db_car[num][0], time]
        else:
            tmpTime = db_car[num][0] + (time - db_car[num][1])
            db_car[num] = [tmpTime, None]
    # print(db_car)
    # 24시 처리
    for key, value in db_car.items():
        if value[1] != None:
            tmpTime = value[0] + (convert("23:59") - value[1])
            db_car[key] = [tmpTime, None]
    # print(db_car)
    # 총기록 -> 요금 반환
    for key, value in db_car.items():
        answer.append([key, payment(fees, value[0])])
    answer.sort(key=lambda x: x[0])
    return list(map(lambda x: x[1], answer))


# print(
#     solution(
#         [180, 5000, 10, 600],
#         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
#          "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#     )
# )

print(
    solution(
        [1, 461, 1, 10]	, ["00:00 1234 IN"]
    )
)
