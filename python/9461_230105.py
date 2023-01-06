# [BOJ] 9461. 파도반 수열  2023-01-05
import sys

T = int(sys.stdin.readline())
for tc in range(T):
    L = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    N = int(sys.stdin.readline())
    if N <= 10:
        print(L[N])
    else:
        for n in range(11, N + 1):
            L.append(L[n- 5] + L[n - 1])
        print(L[N])
