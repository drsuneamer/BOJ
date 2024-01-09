# [BOJ] 3568. iSharp

import sys
input = sys.stdin.readline

dec = input().rstrip().split(' ')

for i in range(1, len(dec)):
    v = ''
    n = ''

    cur = dec[i]

    for c in cur:
        if c not in [',', ';']:
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
                n += c
            else:
                v += c


    print(dec[0] + ''.join(reversed(v)).replace('][', '[]') + ' ' + n + ';')
