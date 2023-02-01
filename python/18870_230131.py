# [BOJ] 18870. 좌표 압축  2023-01-31
import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
LL = sorted(list(set(L[:])))
dict = {}
i = 0

for l in LL:
  dict[l] = i
  i += 1

for l in L:
  print(dict[l], end=" ")
