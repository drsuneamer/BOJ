# [BOJ] 1010. 다리 놓기  2023-01-02


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(M - N) * factorial(N)))