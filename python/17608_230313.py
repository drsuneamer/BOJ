# [BOJ] 17608. 막대기  2023-03-13

import sys
# sys 안 쓰면 시간 초과

N = int(sys.stdin.readline())
L = list(int(sys.stdin.readline()) for _ in range(N))
ans = 1
max = L[-1]

for x in range(N - 1, -1, -1):
  if L[x] > max:
    max = L[x]
    ans += 1

print(ans)