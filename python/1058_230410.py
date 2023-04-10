# [BOJ] <S2> 1058. 친구

import sys
input = sys.stdin.readline

N = int(input())    # 사람의 수 (<= 50)
L = [[] for _ in range(N)]
ans = 0

for i in range(N):
    str = input().rstrip()
    for s in str:
        if s == "Y":
            L[i].append(True)
        else:
            L[i].append(False)

for i in range(N):
    f = 0
    fl = []
    for j in range(N):
        if L[i][j] == True:
            f += 1
        elif i != j:
            for k in range(N):
                if L[i][k] == True and L[j][k] == True:
                    f += 1
                    break

    ans = max(ans, f)


print(ans)
