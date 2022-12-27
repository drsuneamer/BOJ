# [BOJ] 19844. 단어 개수 세기

S = list(input().replace(' ', '-').split('-'))
ans = len(S)
words = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]

for s in S:
    if s[0:2] in words:
        if s[2] in ['a', 'e', 'i', 'o', 'u', 'h']:
            ans += 1
    elif s[0:3] in words:
        if s[3] in ['a', 'e', 'i', 'o', 'u', 'h']:
            ans += 1

print(ans)