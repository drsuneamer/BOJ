# [BOJ] 2075. N번째 큰 수
import heapq

N = int(input())

L = []

for _ in range(N):
    l = list(map(int, input().split()))
    for i in l:
        if len(L) < N:
            heapq.heappush(L, i)
        else:
            if i >= L[0]:
                heapq.heappop(L)
                heapq.heappush(L, i)

print(L[0])