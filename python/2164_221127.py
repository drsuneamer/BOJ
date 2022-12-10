# [BOJ] 2164. 카드2
from collections import deque

N = int(input())
L = deque()

for i in range(1, N + 1):
    L.append(i)

while len(L) != 1:
    L.popleft()
    L.append(L.popleft())

print(L[0])