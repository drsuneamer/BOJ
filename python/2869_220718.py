# [BOJ] 2869. 달팽이는 올라가고 싶다  2022-07-18

A, B, V = map(int, input().split())

a = A - B   # 나눌 수 (하루 이동 값)
b = V - A   # 첫날 값 (나누어지는 수)

if A == V:
    print(1)
elif b % a == 0:
    print(b // a + 1)
else:
    print(b // a + 2)