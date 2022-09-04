# [BOJ] 2108. 통계학
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
L = [0] * N

for i in range(N):
    L[i] = int(input())

D = {}

# 최빈값 구하기
for l in L:
    if l in D:
        D[l] += 1
    else:
        D[l] = 1

M = []
most = 0
for d in D:
    if D[d] > most:
        most = D[d]

for d in D:
    if D[d] == most:
        M.append(d)

L = sorted(L)

print(round(sum(L) / N))
print(L[N//2])
if len(M) == 1:
    print(M[0])
else:
    print(sorted(M)[1])
print(L[-1] - L[0])