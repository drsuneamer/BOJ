# [BOJ] 1475. 방 번호
import math

N = input()
D = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for n in N:
    D[n] += 1

ans = math.ceil((D['6'] + D['9']) / 2)

for d in D:
    if d != '6' and d != '9':
        if D[d] > ans:
            ans = D[d]

print(ans)
