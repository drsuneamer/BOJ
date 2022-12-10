# [BOJ] 2217. 로프 2022-11-26
N = int(input())

a = 0
L = sorted(list(int(input()) for _ in range(N)))

for _ in range(N):
    aa = L[0] * len(L)
    if aa > a:
        a = aa
    L.pop(0)

print(a)
