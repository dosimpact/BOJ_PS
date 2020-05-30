import sys
import math


class City:
    def __init__(self, cost, customer):
        self.cost = cost
        self.customer = customer


C, N = map(int, sys.stdin.readline().split())
cities = [_ for _ in range(N)]
d = [math.inf for _ in range(1101)]
# d(i) i명 > 최소 값

for i in range(N):
    cost, customer = map(int, sys.stdin.readline().split())
    city = City(cost, customer)
    cities[i] = city
# 잘 city 넣어줌.
d[0] = 0
# 각 시티마다. 3 5 = 3원을 들여서 5명

for city in cities:
    # i 고객
    for i in range((1100//city.customer)+1):
        for j in range(1101 - city.customer*i):
            d[j+city.customer*i] = min(d[j+city.customer*i], d[j]+city.cost*i)
print(min(d[C:]))

"""


"""
