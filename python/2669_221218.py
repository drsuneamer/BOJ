# [BOJ] 2669. 직사각형 네개의 합집합의 면적 구하기

L = [[0] * 100 for _ in range(100)]
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            L[i][j] += 1

ans = 0
for i in range(100):
    for j in range(100):
        if L[i][j] == 0:
            ans += 1

print(10000 - ans)