# [BOJ] 1769. 3의 배수
def multiple(x, cnt):
    if len(x) == 1 and int(x) % 3 == 0:
        print(cnt)
        print("YES")
    elif len(x) == 1 and int(x) % 3 != 0:
        print(cnt)
        print("NO")
    else:
        xx = 0
        for i in range(len(x)):
            xx += int(x[i])
        multiple(str(xx), cnt + 1)

X = input()
multiple(X, 0)
