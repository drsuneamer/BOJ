# [BOJ] 2798. 블랙잭
from itertools import combinations

N, M = map(int, input().split())
L = list(map(int, input().split()))
ans = 0

for c in combinations(L, 3):
    if ans < sum(c) <= M:
        ans = sum(c)

print(ans)