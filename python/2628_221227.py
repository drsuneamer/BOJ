# [BOj] 2628. 종이자르기  2022-12-27

h, v = map(int, input().split())
n = int(input())

H = [0]
V = [0]
a1, a2 = 0, 0

for _ in range(n):
    i, j = map(int, input().split())
    if i == 0:
        V.append(j)
    else:
        H.append(j)

H = sorted(H)
H.append(h)
V = sorted(V)
V.append(v)

for i in range(len(H) - 1):
    if H[i+1] - H[i] > a1:
        a1 = H[i+1] - H[i]

for i in range(len(V) - 1):
    if V[i+1] - V[i] > a2:
        a2 = V[i+1] - V[i]

print(a1 * a2)