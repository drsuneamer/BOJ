# [BOJ] 11047. 동전 0  2022-07-26
import sys

N, K = map(int, sys.stdin.readline().split())
L = list(int(sys.stdin.readline().strip()) for _ in range(N))
ans = 0

for i in range(1, N + 1):
    if K >= L[-i]:
        ans += K // L[-i]
        K = K % L[-i]

print(ans)