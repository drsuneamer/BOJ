def d(n):
    global L
    s = n
    while n > 0:
        s += n % 10
        n //= 10
    L.append(s)

L = []
for i in range(1, 10001):
    d(i)

for i in range(1, 10001):
    if i not in L:
        print(i)