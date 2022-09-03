# [BOJ]

N = int(input())
i = 1
n = 1

while n < N:
    n = n + 6 * i
    i += 1

print(i)