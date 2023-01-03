# [BOJ] 2161. 카드1  2022-12-29
import sys

N = int(sys.stdin.readline())
L = [_ for _ in range(1, N + 1)]
ans = []

while len(L) > 0:
    ans.append(L.pop(0))
    if len(L) > 0:
        L.append(L.pop(0))

for a in ans:
    print(a, end=" ")