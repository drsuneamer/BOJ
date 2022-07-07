# [BOJ] 10886. 0 = not cute / 1 = cute

N = int(input())
P = [int(input()) for _ in range(N)]

not_cute = P.count(0)
cute = P.count(1)

if not_cute > cute:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')