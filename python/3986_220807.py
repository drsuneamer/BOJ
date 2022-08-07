# [BOJ] 3986.  좋은 단어  2022-08-07

N = int(input())
ans = 0

for _ in range(N):
    S = [0]
    L = input()
    for l in L:
        if S[-1] == l:
            S.pop(-1)
        else:
            S.append(l)
    if len(S) == 1:
        ans += 1

print(ans)