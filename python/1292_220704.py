# [BOJ] 1292. 쉽게 푸는 문제  2022-07-04

A, B = map(int, input().split())
seq = []

for i in range(50):
    if len(seq) > B:
        break
    else:
        for j in range(i):
            seq.append(i)

ans = 0
for i in range(A - 1, B):
    ans += seq[i]

print(ans)