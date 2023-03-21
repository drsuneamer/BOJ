# [BOJ] <S2> 도영이가 만든 맛있는 음식  2023-03-21

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())  # 재료의 개수
L = []
C = []

for i in range(N):
    L.append(list(map(int, input().split())))

for i in range(1, N + 1):
    cnd = list(combinations(L, i))
    for c in cnd:
        s, b = 1, 0
        for a in c:
            s *= a[0]
            b += a[1]
        C.append(abs(s - b))

print(min(C))
