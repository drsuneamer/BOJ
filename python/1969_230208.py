# [BOJ] 1969. DNA  2023-02-08

N, M = map(int, input().split())
L = [input() for _ in range(N)]
ans = ['', 0]

for m in range(M):
    D = {'T': 0, 'G': 0, 'C': 0, 'A': 0}
    for l in L:
        D[l[m]] += 1
    a, b = '', 0
    for d in D:
        if D[d] >= b:
            b = D[d]
            a = d
    ans[0] += a
    ans[1] += N - b


print(ans[0])
print(ans[1])