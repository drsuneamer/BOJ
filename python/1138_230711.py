# [BOJ] 1138. 한 줄로 서기

import sys
input = sys.stdin.readline

N = int(input())  # 사람의 수
idx = [x for x in range(N)]
ans = [0] * N

people = list(map(int, input().split()))
for i in range(N):
    p = people[i]
    ans[idx[p]] = i + 1
    idx.pop(p)

for a in ans:
    print(a, end=" ")
