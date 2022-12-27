# [BOJ] 16433. 주디와 당근농장

N, R, C = map(int, input().split())
L = [list(['.'] * N) for _ in range(N)]

# 둘다 짝수이거나 둘다 홀수이면
if R % 2 and C % 2 or R % 2 == 0 and C % 2 == 0:
    for i in range(N):
        for j in range(N):
            if i % 2 and j % 2 or i % 2 == 0 and j % 2 == 0:
                L[i][j] = 'v'

else:
    for i in range(N):
        for j in range(N):
            if i % 2 and j % 2 == 0 or i % 2 == 0 and j % 2:
                L[i][j] = 'v'

for i in range(N):
    print("".join(L[i]))