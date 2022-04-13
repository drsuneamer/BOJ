# [BOJ] 2577. 숫자의 개수  2022-04-13

A = int(input())
B = int(input())
C = int(input())

N = str(A * B * C)
L = [0] * 10

for n in N:
    L[int(n)] += 1

for l in L:
    print(l)

