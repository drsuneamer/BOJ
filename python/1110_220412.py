def cnt(start):
    global c
    if start == N:
        return
    else:
        c += 1
        n = start // 10 + start % 10
        new = (start % 10) * 10 + n % 10
        cnt(new)


N = int(input())
nn = N // 10 + N % 10
nnew = (N % 10) * 10 + nn % 10
c = 1   # 횟수 저장

cnt(nnew)
print(c)