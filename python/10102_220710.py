# [BOJ] 10102. 개표

V = int(input())
C = input()


A = C.count('A')
B = C.count('B')

if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')