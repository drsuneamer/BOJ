M = int(input())
N = int(input())
ssum = 0
mmin = 10000


for i in range(M, N+1):
    L = []
    for j in range(1, i+1):
        if i % j == 0:
            L.append(j)
    if len(L) == 2:
        ssum += i
        if i < mmin:
            mmin = i

if ssum == 0:
    print(-1)
else:
    print(ssum)
    print(mmin)