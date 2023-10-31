# [BOJ] 28107. 회전초밥

import sys
input = sys.stdin.readline

# N: 손님의 수, M: 초밥의 수 
N, M = map(int, input().split())

ans = [0] * N
orders = [[] for _ in range(200001)]

for i in range(N):
    cur = list(map(int, input().split()))
    cur.pop(0)
    for c in cur:
        orders[c].append(i)

mades = sorted(list(map(int, input().split())))

for m in mades:
    if len(orders[m]) > 0:
        ans[orders[m].pop(0)] += 1

for a in ans:
    print(a, end=" ")
