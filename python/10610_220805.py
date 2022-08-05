# [BOJ] 10610. 30  2022-08-05

N = input()
L = []
ans = ''
for n in N:
    L.append(int(n))

if sum(L) % 3 != 0 or 0 not in L:     # 3의 배수가 될 수 있는지 확인
    print(-1)

else:
    LL = sorted(L, reverse=True)
    for l in LL:
        ans += str(l)

print(ans)