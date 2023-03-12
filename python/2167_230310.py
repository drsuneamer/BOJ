# [BOJ] 2167. 2차원 배열의 합
import sys

N, M = map(int, sys.stdin.readline().split())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
A = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        A[i+1][j+1] = L[i][j] + A[i+1][j] + A[i][j+1] - A[i][j]

K = int(input())
for _ in range(K):
    a, b, c, d = map(int, input().split())
    print(A[c][d] - A[a-1][d] - A[c][b-1] + A[a-1][b-1])

