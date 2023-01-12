# [BOJ] 11659. 구간 합 구하기 4  2023-01-12
import sys

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    L[i] = L[i - 1] + L[i]

for tc in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(L[j - 1])
    elif i == j:
        print(L[j - 1] - L[j - 2])
    else:
        print(L[j - 1] - L[i - 2])