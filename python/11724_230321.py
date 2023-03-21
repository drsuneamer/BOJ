# [BOJ] <S2> 11724. 연결 요소의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def DFS(v):
    visited[v] = 1
    for n in L[v]:
        if visited[n] == False:
            DFS(n)


N, M = map(int, input().split())
L = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

ans = 0

for i in range(1, N + 1):
    if visited[i] == False:
        DFS(i)
        ans += 1

print(ans)
