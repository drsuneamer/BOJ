# [BOJ] 10026. 적록색약
from collections import deque

def bfs():
    while q:
        a, b = q.popleft()

        for i in range(4):
            ni, nj = a + di[i], b + dj[i]
            if 0 <= ni < N and 0 <= nj < N and L[a][b] == L[ni][nj] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj])



N = int(input())
L = [list(input()) for _ in range(N)]


di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

# 적록색약이 아닌 경우

q = deque()
ans1 = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            q.append([i, j])
            visited[i][j] = 1
            bfs()
            ans1 += 1


# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if L[i][j] == 'R':
            L[i][j] = 'G'

ans2 = 0
q = deque()
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            q.append([i, j])
            bfs()
            ans2 += 1

print(ans1, ans2)