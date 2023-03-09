# [BOJ] 2018. 수들의 합 5

N = int(input())
M = (N // 2) + 1
ans = 1

i, j = 1, 1

while j <= M and i < M:
    n = ((j + i) / 2) * (j - i + 1)
    if n == N:
        ans += 1
        j += 1
    elif n > N:
        i += 1
    elif n < N:
        j += 1
        
print(ans)