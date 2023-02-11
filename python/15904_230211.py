# [BOJ] 15904. UCPC는 무엇의 약자일까?  2023-02-11

S = input()
ans = ''

for s in S:
    if len(ans) == 4:
        break
    else:
        if ans == '' and s == 'U':
            ans += s
        if ans == 'U' and s == 'C':
            ans += s
        if ans == 'UC' and s == 'P':
            ans += s
        if ans == 'UCP' and s == 'C':
            ans += s

if ans == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')