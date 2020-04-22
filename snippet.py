"""
-트라이 자료구조 구현하기
-행렬 회전하기 시계방향 90됴 ( 노말버전, 파이썬 버전 )
-다음 순열 구현하기 ✅
-비트마스크로 모든 집합 순회하기 (1182 BOJ) 

"""

from collections import deque
import sys

dq = deque(['.', 'c', '.', 'c'])
print(dq)  # deque(['.', 'c', '.', 'c'])

dq.rotate(1)
print(dq)  # deque(['c', '.', 'c', '.'])

dq.rotate(-1)
print(dq)  # deque(['.', 'c', '.', 'c'])
