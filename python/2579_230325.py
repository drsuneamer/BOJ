# [BOJ] <S3> 2579. 계단 오르기

N = int(input())    # 계단의 개수 (1 <= N <=300)
L = [int(input()) for _ in range(N)]    # 전체 계단의 점수

'''
얻을 수 있는 총 점수의 최대값 출력하기

한 번에 한 계단 또는 두 계단
연속된 세 계단 밟으면 안 됨 (시작점 포함 X)
마지막 반드시 밟아야 함
'''

if N <= 2:
    print(sum(L))

else:
    dp = [0] * N

    dp[0] = L[0]
    dp[1] = L[0] + L[1]
    dp[2] = max(L[2] + L[1], L[0] + L[2])

    for i in range(3, N):
        dp[i] = max(dp[i - 2] + L[i], dp[i - 3] + L[i - 1] + L[i])
    print(dp[N - 1])

'''
반례
10
3
5
10
9
2
1
2
5
2
9

정답: 37
3 x 10 9 x 1 x 5 x 9

6
1
1
2
2
1
1
정답: 6

'''
