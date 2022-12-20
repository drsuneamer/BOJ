# [BOJ] 1003. 피보나치 함수  2022-12-12

T = int(input())
dp = [[1, 0], [0, 1]]
for i in range(2, 43):

    dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])

for tc in range(T):
    N = int(input())

    print(dp[N][0], dp[N][1])

