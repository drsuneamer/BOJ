# [BOJ] 1620. 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, sys.stdin.readline().split())
P = {}

for i in range(1, N+1):
    P[i] = sys.stdin.readline().strip()

PP = dict(map(reversed, P.items()))
for _ in range(M):
    a = sys.stdin.readline().strip()
    try:
        print(P[int(a)])
    except:
        print(PP[a])