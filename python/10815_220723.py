# [BOJ] 10815. 숫자 카드  2022-07-23
import sys

N = int(sys.stdin.readline())
L1 = set(sys.stdin.readline().split())

M = int(sys.stdin.readline())
L2 = list(sys.stdin.readline().split())

for l in L2:
    if l in L1:
        print(1, end=" ")
    else:
        print(0, end=" ")