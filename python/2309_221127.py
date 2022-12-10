# [BOJ] 2309. 일곱 난쟁이
from itertools import combinations

L = sorted(list(int(input()) for _ in range(9)))
C = list(combinations(L, 7))
ans = []

for c in C:
    if sum(c) == 100:
        ans = c
        break

for a in sorted(ans):
    print(a)