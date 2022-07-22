# [BOJ] 2839. 설탕 배달  2022-07-22

N = int(input())

if N == 3 or N == 1:
    print(1)
elif N == 4:
    print(-1)
else:   # N이 5보다 큰 경우부터 시작
    s = N // 5
    while s >= 1:
        if (N - s * 5) % 3 == 0:
            print(s + (N - s * 5) // 3)
            break
        else:
            s -= 1
    else:
        if N % 3 == 0:
            print(N // 3)
        else:
            print(-1)

