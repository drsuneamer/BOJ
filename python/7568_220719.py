# [BOJ] 7568. 덩치

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    ans = 1

    for j in range(N):
        if L[j][0] > L[i][0] and L[j][1] > L[i][1]:
            ans += 1

    print(ans, end=" ")