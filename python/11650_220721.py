# [BOJ] 11650. 좌표 정렬하기

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

LL = sorted(L, key=lambda x: (x[0], x[1]))

for i in range(len(LL)):
    for j in range(2):
        print(LL[i][j], end=" ")
    print()