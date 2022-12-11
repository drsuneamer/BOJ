# [BOJ] 1676. 팩토리얼 0의 개수  2022-12-11
import math

N = int(input())
n = str(math.factorial(N))
ans = 0

for i in range(len(n) - 1, -1, -1):
    if n[i] == '0':
        ans += 1
    else:
        break

print(ans)