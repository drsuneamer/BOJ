# [BOJ] 11651. 좌표 정렬하기 2

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

LL = sorted(L, key=lambda x: (x[1], x[0]))

for l in LL:
    print(l[0], l[1])