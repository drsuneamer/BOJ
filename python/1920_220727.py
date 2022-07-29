# [BOJ] 1920. 수 찾기
import sys

N = int(sys.stdin.readline())
L = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
LL = list(map(int, sys.stdin.readline().split()))

for ll in LL:
    if ll in L:
        print(1)
    else:
        print(0)