# [BOJ] 10250. ACM 호텔  2022-11-26

T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())

    h = N % H
    if h == 0:
        h = H
    if N < H:
        h = N

    if N % H == 0:
        w = N // H
    else:
        w = N // H + 1

    print(str(h)+format(w, '02'))
