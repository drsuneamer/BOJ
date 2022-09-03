# [BOJ] 2609. 최대공약수와 최소공배수

A, B = map(int, input().split())

s = min(A, B)
l = max(A, B)

for i in range(s, 0, -1):
    if A % i == 0 and B % i == 0:
        print(i)
        break
i = 1
while 1:
    if l * i % s == 0:
        print(l * i)
        break
    else:
        i += 1