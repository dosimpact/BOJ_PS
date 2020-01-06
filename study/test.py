
from itertools import combinations

N = int(input())
S = [[]]* N
for i in range(N):
	S[i] = list(map(int, input().split()))

people = list(range(1, N+1))

def func():
	global min_score

	for link in combinations(people, N//2):
		link_mem = list(set(link))
		start_mem = list(set(people) - set(link))

		link_comb_list = list(combinations(link_mem, 2))
		start_comb_list = list(combinations(start_mem, 2))
		
		link_score = 0
		for x,y in link_comb_list:
			link_score += (S[x-1][y-1] + S[y-1][x-1])

		start_score = 0
		for x,y in start_comb_list:
			start_score += (S[x-1][y-1] + S[y-1][x-1])

		min_score = min(min_score, abs(link_score - start_score))

if __name__ == '__main__':
	min_score = 100
	func()
	print(min_score)
