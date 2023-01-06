# [BOJ] 2870. 수학 숙제  2023-01-03
import sys

N = int(sys.stdin.readline())
A = []
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for _ in range(N):
    s = sys.stdin.readline()
    a = ''
    i = 0
    for ss in s:
        if ss in num:
            a += ss
        else:
            a += ','

    l = a.split(',')
    A += [int(v) for v in l if v != '']

for x in sorted(A):
    if len(str(x)) > 1 and str(x)[0] == '0':
        print(x[1:])
    else:
        print(x)
