# [BOJ] 14929. 귀찮아
import sys

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
LL = [L[0]]

for i in range(1, n):
    LL.append(L[i] + LL[i - 1])
ans = 0

for i in range(n - 1):
    ans += L[i] * (LL[n - 1] - LL[i])

print(ans)