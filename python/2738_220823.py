# [BOJ] 2738. 행렬 덧셈

N, M = map(int, input().split())    # N: 행렬의 크기, M: 행렬의 원소 개수

L = [list(map(int, input().split())) for _ in range(N)]
L2 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        L[i][j] += L2[i][j]

for i in range(N):
    for j in range(M):
        print(L[i][j], end=" ")
    print()