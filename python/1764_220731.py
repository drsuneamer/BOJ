# [BOJ] 1764. 듣보잡  2022-07-31
import sys

N, M = map(int, sys.stdin.readline().split())
L = set(sys.stdin.readline().strip() for _ in range(N))
ans = []

for _ in range(M):
    m = input()
    if m in L:
        ans.append(m)

print(len(ans))
for a in sorted(ans):
    print(a)
