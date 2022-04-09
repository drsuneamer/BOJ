# [BOJ] 2667. 단지 번호 붙이기  2022-04-09

def bfs(a, b, n):
    q = []
    q.append([a, b])
    visited[a][b] = 1
    arr[a][b] = n
    cnt = 1     # 단지 수

    while q:
        i, j = q.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                arr[ni][nj] = n
                visited[ni][nj] = 1
                cnt += 1
    R.append(cnt)   # 완료되면 단지 수 저장


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
num = 0     # 단지 번호
R = []   # 단지 수 저장할 리스트

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            num += 1    # 단지 번호 1 증가
            bfs(i, j, num)

R.sort()
print(num)
for i in range(len(R)):
    print(R[i])