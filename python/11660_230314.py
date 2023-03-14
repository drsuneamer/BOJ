# [BOJ] 11660. 구간 합 구하기 5  2023-03-14

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N: 표의 크기
# M: 합을 구해야 하는 횟수 (tc)

L = [[0] * (N + 1) for _ in range(N + 1)]

NL = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  for j in range(N):
    L[i+1][j+1] = L[i][j+1] + L[i+1][j] + NL[i][j] - L[i][j]

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  print(L[x2][y2] - L[x1-1][y2] - L[x2][y1-1] + L[x1-1][y1-1])