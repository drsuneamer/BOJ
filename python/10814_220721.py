# [BOJ] 10814. 나이순 정렬

N = int(input())
L = [[0] * 3 for _ in range(N)]

for i in range(N):
    L[i][0], L[i][1] = input().split()
    L[i][2] = i

LL = (sorted(L, key=lambda x: (int(x[0]), x[2])))

for i in range(N):
    print(LL[i][0], LL[i][1])