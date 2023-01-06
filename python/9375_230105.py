# [BOJ] 9375. 패션왕 신해빈  2023-01-05
import sys

T = int(sys.stdin.readline())
for tc in range(T):
    D = {}
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        if b in D:
            D[b].append(a)
        else:
            D[b] = [a]

    ans = 1
    for d in D:
        ans *= len(D[d]) + 1
    print(ans - 1)  # 아무것도 안 입는 경우 제외