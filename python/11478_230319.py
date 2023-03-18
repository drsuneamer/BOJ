# [BOJ] S3> 11478. 서로 다른 부분 문자열의 개수
import sys
from itertools import combinations
input = sys.stdin.readline

s = input()
idx = [x for x in range(len(s))]
comb = list(combinations(idx, 2))
ans = set()

for c in comb:
    a = s[c[0]:c[1]]
    ans.add(a)

print(len(ans))
