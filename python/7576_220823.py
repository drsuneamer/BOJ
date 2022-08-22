# [BOJ] 7576. 토마토
from collections import deque
def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            ni, nj = x + di[i], y + dj[i]
            if 0 <= ni < N and 0 <= nj < M and tomatoes[ni][nj] == 0:
                tomatoes[ni][nj] = tomatoes[x][y] + 1
                q.append([ni, nj])


M, N = map(int, input().split())    # M: 가로, N: 세로
tomatoes = [list(map(int, input().split())) for _ in range(N)]
q = deque()

start = [0, 0]
for i in range(N):      # 시작점 구하기
    for j in range(M):
        if tomatoes[i][j] == 1:
            start = [i, j]
            q.append(start)


# 오른쪽, 아래, 왼쪽, 위
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

bfs()


ans = max(map(max, tomatoes)) - 1

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            ans = -1

print(ans)