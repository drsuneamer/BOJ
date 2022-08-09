# [BOJ] 11656. 접미사 배열  2022-08-08

S = input()
L = []

for i in range(len(S)):
    L.append(S[i:len(S)])

LL = sorted(L)
for l in LL:
    print(l)