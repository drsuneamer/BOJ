# [BOJ] 14916. 거스름돈

N = int(input())
m = N // 5

while 1:
    if (N - (m * 5)) % 2 == 0:
        ans = m + ((N - (m * 5)) // 2)
        break
    elif m <= 0:
        ans = -1
        break
    else:
        m -= 1

print(ans)