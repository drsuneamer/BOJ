# [BOJ] 2530. 인공지능 시계  2022-07-06

A, B, C = map(int, input().split())
D = int(input())

# 두 번째 줄에는 요리하는 데 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위로 주어진다.
if D >= 86400:
    D %= 86400

hour, minute, second = 0, 0, 0

if D >= 60:
    m = D // 60
    second = D % 60     # 나머지는 바로 초로 저장
    if m >= 60:
        hour = m // 60
        minute = m % 60
    else:
        minute = m
else:   # 60 이하인 경우 바로 초로 저장
    second = D

C = C + second
if C >= 60:
    C -= 60
    B += 1

B = B + minute
if B >= 60:
    B -= 60
    A += 1

A = A + hour
if A >= 24:
    A -= 24

print(A, B, C)