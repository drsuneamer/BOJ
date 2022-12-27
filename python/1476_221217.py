# [BOJ] 1476. 날짜 계산

# E <= 15, S <= 28, M <= 19
E, S, M = map(int, input().split())
A = [E, S, M]

i = 0
while 1:
    LL = [1, 1, 1]
    LL[0] += i
    LL[1] += i
    LL[2] += i
    if LL[0] > 15:
        LL[0] = i % 15 + 1
    if LL[1] > 28:
        LL[1] = i % 28 + 1
    if LL[2] > 19:
        LL[2] = i % 19 + 1

    if LL == A:
        print(i + 1)
        break
    else:
        i += 1


