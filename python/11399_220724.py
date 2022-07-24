# [BOJ] 11399. ATM  2022-07-24
import sys

N = int(sys.stdin.readline())
P = sorted(list(map(int, sys.stdin.readline().split())))

ans = 0
start = 0
for i in range(N):
    start += P[i]
    ans += start

print(ans)