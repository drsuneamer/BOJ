# [BOJ] 1012. 유기농 배추
from collections import deque

def BFS(i, j):
    Q = deque()
    Q.append([i, j])
    # 오른쪽, 아래, 왼쪽, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, -0]

    while Q:
        ii, jj = Q.popleft()
        for k in range(4):
            ni, nj = ii + di[k], jj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 1:
                field[ni][nj] = 0
                Q.append([ni, nj])


T = int(input())
for _ in range(T):      # M: 가로, N: 세로
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    ans = 0
    for _ in range(K):
        i, j = map(int, input().split())
        field[j][i] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                BFS(i, j)
                ans += 1

    print(ans)
