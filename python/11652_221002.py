# [BOJ] 11652. 카드

N = int(input())

D = {}
L = []

for i in range(N):
    n = int(input())
    if n in D:
        D[n] += 1
    else:
        D[n] = 1

v = max(D.values())
for d in D:
    if D[d] == v:
        L.append(d)

print(min(L))