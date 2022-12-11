# [BOJ] 2231. 분해합

N = int(input())

D = {}

for i in range(1, N + 1):
    a = i
    for j in range(len(str(i))):
        a += int(str(i)[j])
    D[i] = a

ans = 0

for i in range(1, N + 1):
    if D[i] == N:
        ans = i
        break

print(ans)