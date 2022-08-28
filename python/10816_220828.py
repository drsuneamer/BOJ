# [BOJ] 10816. 숫자 카드 2
import sys

N = int(sys.stdin.readline())   # 가지고 있는 숫자 카드의 개수
D = {}
L = list(map(int, input().split()))

for l in L:
    if l in D:
        D[l] += 1
    else:
        D[l] = 1

M = int(sys.stdin.readline())
L2 = list(map(int, input().split()))

for l in L2:
    if l in D:
        print(D[l], end=" ")
    else:
        print(0, end=" ")