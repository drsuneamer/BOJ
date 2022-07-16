# [BOJ] 10867. 중복 빼고 정렬하기  2022-07-16

N = int(input())
L = set(map(int, input().split()))
LL = sorted(L)

for i in range(len(LL)):
    if i != len(LL) - 1:
        print(LL[i], end=' ')
    else:
        print(LL[i])