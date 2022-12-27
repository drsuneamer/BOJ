# [BOJ] 2023. 신기한 소수
import sys, math

N = int(sys.stdin.readline())    # 1 <= N <= 8


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def f(n):
    if len(str(n)) == N and prime(n):
        print(n)
    else:
        if prime(n):
            for i in range(1, 10, 2):
                nn = 10 * n + i
                f(nn)


f(2)
f(3)
f(5)
f(7)