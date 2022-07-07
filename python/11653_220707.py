# [BOJ] 11653. 소인수분해  2022-07-07

N = int(input())
i = 2

if N != 1:
    while N != 1:
        if N % i == 0:
            N //= i
            print(i)
        else:
            i += 1
