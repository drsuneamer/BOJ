# [BOJ] 1929. 소수 구하기  2022-04-25

def prime(m, n):
    # m 이상 n 이하의 소수 출력
    sieve = [1] * (n + 1)

    for i in range(2, n + 1):
        if sieve[i] == 1:
            if i >= m:
                print(i)
            for j in range(i + i, n + 1, i):
                sieve[j] = 0


M, N = map(int, input().split())
prime(M, N)