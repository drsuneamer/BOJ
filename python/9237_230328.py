# [BOJ] <S5> 9237. 이장님 초대

import sys
input = sys.stdin.readline

N = int(input())
L = sorted(list(map(int, input().split())), reverse=True)

maxV = 0

for i in range(N, 0, -1):
    maxV = max(maxV, L[N - i] - i)

print(maxV + N + 2)
