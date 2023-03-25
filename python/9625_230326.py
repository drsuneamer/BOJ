# [BOJ] <S5> 9625. BABBA

K = int(input())
dp = [[1, 0], [0, 1]]

for i in range(2, K + 1):
    a = dp[i - 1][1]
    b = dp[i - 1][1] + dp[i - 1][0]
    dp.append([a, b])

print(dp[K][0], dp[K][1])
