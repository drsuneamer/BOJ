# [BOJ] 16435. 스네이크버드  2023-03-16

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
H = sorted(list(map(int, input().split())))

for h in H:
    if L >= h:
        L += 1
    else:
        break

print(L)
