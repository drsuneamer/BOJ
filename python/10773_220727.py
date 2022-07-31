# [BOJ] 10773. 제로  2022-07-27
import sys

K = int(sys.stdin.readline())
L = []
for _ in range(K):
    i = int(sys.stdin.readline())
    if i == 0:
        L.pop()
    else:
        L.append(i)

print(sum(L))