# [BOJ] 2475. 검증수

L = list(map(int, input().split()))
ans = 0
for l in L:
    ans += l ** 2

print(ans % 10)