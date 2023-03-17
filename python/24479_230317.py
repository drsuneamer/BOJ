# [BOJ] <S2> 24479. 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(r):
    global cnt
    cnt += 1
    node = graph[r]
    ans[r] = cnt
    visited[r] = 1

    for n in node:
      if visited[n] == 0:
          DFS(n)
    return

  
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
ans = [0] * (N + 1)
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    if (len(g) > 0):
        g = g.sort()

DFS(R)

for i in range(1, N + 1):
    print(ans[i])
