# [BOJ] 2178. 미로 탐색  2022-07-29
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
Q = deque()
Q.append((0, 0))

count = [[0] * M for _ in range(N)]

# 오른쪽, 아래, 왼쪽, 위
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

while Q:
    (a, b) = Q.popleft()

    for i in range(4):
        ni, nj = a + di[i], b + dj[i]

        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1:
            Q.append((ni, nj))
            maze[ni][nj] = maze[a][b] + 1

print(maze[N - 1][M - 1])