# [BOJ] 16948. 데스 나이트  2023-04-27

import sys

input = sys.stdin.readline
from collections import deque


# 최소값: bfs 사용
def bfs(i, j):
  global ans
  Q = deque()
  visited[i][j] = 1
  Q.append([i, j, 0])

  di = [-2, -2, 0, 0, 2, 2]
  dj = [-1, 1, -2, 2, -1, 1]

  while Q:
      a, b, c = Q.popleft()
      
      if a == r2 and b == c2:
          ans = c
          return

      for k in range(6):
          ni, nj = a + di[k], b + dj[k]
          if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
              visited[ni][nj] = 1
              Q.append([ni, nj, c + 1])
              


N = int(input())  # 체스판의 크기: N * N
r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * N for _ in range(N)]
ans = -1

bfs(r1, c1)
print(ans)
