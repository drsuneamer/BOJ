# [BOJ] 1417. 국회의원 선거  2023-02-07

N = int(input())
D = int(input())
L = [int(input()) for _ in range(N - 1)]
ans = 0

while L:    # while 1로 할 경우 전체 주민이 1명인 경우가 있어 에러 발생
    L = sorted(L, reverse=True)
    if L[0] >= D:
        D += 1
        ans += 1
        L[0] -= 1
    else:
        break

print(ans)