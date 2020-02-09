# EOF 까지 읽어서, 뛰어쓰기는 제거하고 ,로 나눠서 리스트를 반환후 더한값을 출력하기
# https://www.acmicpc.net/problem/10823
import sys

nlist = [int(x) for x in sys.stdin.read().replace('\n', '').split(',')]
print(sum(nlist))
