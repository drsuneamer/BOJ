X = int(input())

i = 1
a = 0
while a < X:
    a += i
    i += 1

start_num = a - i + 2

a = 1
b = i - 1
for _ in range(X - start_num):
    a += 1
    b -= 1

if (i - 1) % 2:
    print(f'{b}/{a}')
else:
    print(f'{a}/{b}')
