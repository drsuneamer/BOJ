# [BOJ] 1269. 대칭 차집합  2023-01-03
import sys

a, b = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

AA = set(x for x in A if x not in B)
BB = set(x for x in B if x not in A)

print(len(AA) + len(BB))