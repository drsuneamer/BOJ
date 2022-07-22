# [BOJ] 1712. 손익분기점
import sys

# A: 고정비용, B: 가변비용, C: 가격
A, B, C = map(int, sys.stdin.readline().split())

if C <= B:
    print(-1)
else:
    print(A // (C - B) + 1)