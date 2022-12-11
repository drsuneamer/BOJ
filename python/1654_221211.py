# [BOJ] 1654. 랜선 자르기  2022-12-11

# K: 가지고 있는 랜선의 개수, N: 필요한 랜선의 개수
K, N = map(int, input().split())
L = list(int(input()) for _ in range(K))

min_v = 1
max_v = max(L)
ans = 0

while min_v <= max_v:
    mid = (min_v + max_v) // 2
    a = 0
    for l in L:
        a += l // mid

    if a < N:
        max_v = mid - 1

    else:
        min_v = mid + 1

print(min(min_v, max_v))