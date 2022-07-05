# [BOJ] 2563. 색종이  2022-07-05

W = [[0] * 100 for _ in range(100)]
N = int(input())    # 색종이의 수
for i in range(N):
    S, E = map(int, input().split())

    for j in range(100 - E - 10, 100 - E):
        for k in range(S, S + 10):
            W[j][k] += 1
ans = 0
for i in range(100):
    for j in range(100):
        if W[i][j] != 0:
            ans += 1

print(ans)
