# [BOJ] 2941. 크로아티아 알파벳  2022-04-28

S = input()

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in alphabets:
    if a in S:
        S = S.replace(a, 'x')

print(len(S))