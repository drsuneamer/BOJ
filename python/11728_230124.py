# [BOJ] 11728. 배열 합치기
import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

for a in sorted(A + B):
    print(a, end=" ")