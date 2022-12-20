# [BOJ] 9095. 1, 2, 3 더하기

T = int(input())
dp = [0, 1, 2, 4]
for i in range(4, 14):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for tc in range(1, T + 1):
    n = int(input())
    print(dp[n])