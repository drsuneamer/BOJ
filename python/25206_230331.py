# [BOJ] <25206. 너의 평점은

import sys
input = sys.stdin.readline

g = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0}

s = 0
cnt = 0

for i in range(20):
    a, b, c = map(str, input().split())
    if c != 'P':
      s += float(b) * g[c]
      cnt += float(b)

print(s / cnt)
