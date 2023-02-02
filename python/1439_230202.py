# [BOJ] 1439. 뒤집기

S = input()
cnt = 0
for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        cnt += 1

if S[0] == S[-1]:
    print(cnt // 2)
else:
    print(cnt // 2 + 1)