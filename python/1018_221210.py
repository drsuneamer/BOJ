# [BOJ] 1018. 체스판 다시 칠하기

N, M = map(int, input().split())    # N: 세로 길이
B = [list(map(str, input())) for _ in range(N)]
ans = N * M

for i in range(N - 7):   # x좌표
    for j in range(M - 7):   # y좌표
        a = 0
        b = 0
        # W로 시작하는 경우
        for di in range(8):
            for dj in range(8):
                if di % 2:  # 홀수행
                    if dj % 2:   # 홀수열
                        if B[i + di][j + dj] != 'W':
                            a += 1
                        else:
                            b += 1
                    else:    # 짝수열
                        if B[i + di][j + dj] != 'B':
                            a += 1
                        else:
                            b += 1
                else:  # 짝수행
                    if dj % 2:  # 홀수열
                        if B[i + di][j + dj] != 'B':
                            a += 1
                        else:
                            b += 1
                    else:  # 짝수열
                        if B[i + di][j + dj] != 'W':
                            a += 1
                        else:
                            b += 1
        if min(a, b) <= ans:
            ans = min(a, b)

print(ans)