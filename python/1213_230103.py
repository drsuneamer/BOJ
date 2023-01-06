# [BOj] 1213. 팰린드롬 만들기  2023-01-03

S = input()
D = {}
ans = ''
plus = ''
p = 1

for s in S:
    if s in D:
        D[s] += 1
    else:
        D[s] = 1

D = sorted(D.items())
odd = 0
for d in D:
    if d[1] % 2:
        odd += 1
    if odd > 2:
        break

if odd > 1:
    p = 0

if p == 1:
    for d in D:
        ans += d[0] * (int(d[1]) // 2)
        if d[1] % 2:
            plus += d[0]
    print(ans+plus+ans[::-1])
else:
    print("I'm Sorry Hansoo")