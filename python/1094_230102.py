# [BOJ] 1094. 막대기
import sys

X = int(sys.stdin.readline())
L = [64]

while sum(L) > X:
    l = L.pop(-1)
    L.append(l // 2)
    L.append(l // 2)

    if sum(L[:-1]) >= X:
        L.pop(-1)

print(len(L))
