# [BOJ] 1182. 부분수열의 합  2023-03-16

import sys
input = sys.stdin.readline


def combination(r, l, start):
    global ans
    if r == l:
        if sum(selected) == S:
            ans += 1
        return
    
    for i in range(start, N):
        if visited[i]: continue
    
        selected[r] = L[i]
        visited[i] = True
        combination(r + 1, l, i + 1)
        visited[i] = False
    


N, S = map(int, input().split())
L = list(map(int, input().split()))
ans = 0

for i in range(1, N + 1):
    selected = [0] * i
    visited = [0] * N
    combination(0, i, 0)
    
print(ans)
