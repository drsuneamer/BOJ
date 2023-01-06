# [BOJ] 1049. 기타줄  2022-01-03
import sys

N, M = map(int, sys.stdin.readline().split())
a, b, c = N // 6, N % 6, N // 6 + 1
aa, bb = 1000, 1000

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i < aa:
        aa = i
    if j < bb:
        bb = j

print(min(a * aa + b * bb, c * aa, N * bb))
