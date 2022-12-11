# [BOJ] 2805. 나무 자르기

# N: 나무의 수, M: 가져가고자 하는 나무의 길이
N, M = map(int, input().split())
L = list(map(int, input().split()))

# 적어도 M 미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
min_v = 0
max_v = max(L)

while min_v <= max_v:
    mid = (min_v + max_v) // 2
    a = 0
    for l in L:
        if l > mid:
            a += l - mid
    if a >= M:
        min_v = mid + 1
    else:
        max_v = mid - 1

print(max_v)