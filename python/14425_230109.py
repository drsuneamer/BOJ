# [BOJ] 14425. 문자열 집합
import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
ans = 0

for i in range(N):
    S.add(sys.stdin.readline().rstrip())

for i in range(M):
    if sys.stdin.readline().rstrip() in S:
        ans += 1

print(ans)
