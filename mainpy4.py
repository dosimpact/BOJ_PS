
# 1번

치킨앞에서 모든게 용서가 된다.


# 2번

input: 단말기 id, 게이트 입구, 게이트 출구
Output: 통행요금, 잔액
Step:
1.게이트 입구에 들어서면 해당 입구를 저장.
2.단말기 서버에서 해당 단말기 정보와 차량 진입을 전송받음
3.게이트 출구에서 해당 단말기 정보와 차량 진출을 전송 받음
4.입구와 출구의 거리에 다른 통행 요금을 계산
5.충전된 금액에서 통행 요금을 빼서 잔액을 계산
6.통행 요금과, 잔액을 알려줌


# 3번

1. card[i] = n
2. num == card[i]
3. flag = True
4. break
5. flag == False

# 4번


1. num[i] = n
2. num
3. 5
4. 3
5. i//1000 == first and i % 10 == last

# 5번

49
1
True
a // b = 3-안녕  # 숭실

# 6번

se = str(input("성별을 입력하세요.(여아/남아)"))
we = int(input("몸무게를 입력하세요.")) ❌
he = int(input("신장(cm)을 입력해주세요.")) ❌

if se == '여아' and (12 <= we and we <= 22):
    if 91 <= he and he <= 100:
        print('7호를 추천합니다.')
    elif 101 <= he and he <= 110:
        print('9호를 추천합니다.')
    elif 111 < he and he <= 120:
        print('11호를 추천합니다.')
    else:
        print("해당 사이즈가 없습니다.")

# 7번
for i in range(start, end+1, 1):
    if i % 2 == 0 or i % 5 == 0:
        print(i)
        hap += i

# 8번
True
if num == 0:
    break
else:  # ❌
    hap += num


# 9번 ❌

weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
for i in range(len(nID)):
    Multi.append(nID[i]*weight[i])


# 10번


1. menu, quntity
2. 인덱스 = 메뉴[menu]
3. 전체금액 = 금액[menu]*quntity ❌
4. (인덱스, 전체금액)
5. Price(menu, quntity)

# 11번

for i in range(len(가수)):
    for j in range(i, len(가수)):
        tmp = 가수[j]
        가수[j] = 가수[i]
        가수[i] = tmp
