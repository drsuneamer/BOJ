# [BOJ] 1789. 수들의 합

S = int(input())
s = 0

for i in range(S + 1):
    s += i
    if s == S:
        print(i)
        break
    elif s > S:
        print(i - 1)
        break