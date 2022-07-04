# [BOJ] 2455. 지능형 기차  2022-07-04

ans = 0
p = 0

for i in range(4):
    a, b = map(int, input().split())
    p -= a
    p += b
    if p >= ans:
        ans = p

print(ans)