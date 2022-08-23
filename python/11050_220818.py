# [BOJ] 11050. 이항 계수 1
from itertools import combinations

N, K = map(int, input().split())
L = [i for i in range(1, N + 1)]

print(len(list(combinations(L, K))))