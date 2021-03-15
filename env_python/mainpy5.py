from sys import stdin


input = stdin.readline


N = int(input())
data = [list(map(int, input().split())) for i in range(N)]
data.sort(key=lambda x: (x[1], x[0]))

ltime, ans = 0, 0
for d in data:
    if d[0] >= ltime:
        ans += 1
        ltime = d[1]
print(ans)

"""
✅ 회의 종료 시간이 같은 회의중에 , 2번까지 세이브 하는 경우 있다.
3
2 2
1 2
2 3
>2 ( 첫번째 정렬을 안할때  (2,2)-(2,3) )
>3 ( 첫번째 정렬을 할때   (1,2)-(2,2)-(2,3) )

1
1 200

2
1 1
1 1

5
0 1
1 2
2 2
2 3
3 3

6
2 13
3 5
3 4
3 3
4 7
4 6


"""