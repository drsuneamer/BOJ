# [BOJ] 11004. K번째 수  2023-01-03
import sys

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

print(sorted(L)[K - 1])