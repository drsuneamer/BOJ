# [BOJ] 1463. 1로 만들기
import sys

X = int(sys.stdin.readline())
L = [0] * (X + 1)

for i in range(2, X + 1):
    if i % 2 == 0 and i % 3 == 0:
        L[i] = min(L[i - 1] + 1, L[i // 2] + 1, L[i // 3] + 1)
    elif i % 2 == 0:
        L[i] = min(L[i - 1] + 1, L[i // 2] + 1)
    elif i % 3 == 0:
        L[i] = min(L[i - 1] + 1, L[i // 3] + 1)
    else:
        L[i] = L[i - 1] + 1

print(L[X])