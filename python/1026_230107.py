# [BOJ] 1026. 보물  2023-01-07
import sys

ans = 0
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

for i in range(N):
    ans += A[i] * B[i]

print(ans)