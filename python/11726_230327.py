# [BOJ] <S3> 11726. 2xn 타일링

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n

if n == 1:
    print(1)  
else:
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    print(dp[n - 1] % 10007)
