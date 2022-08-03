# [BOJ] 10825. 국영수
import sys

N = int(input())
L = [list(sys.stdin.readline().split()) for _ in range(N)]
LL = sorted(L, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for l in LL:
    print(l[0])