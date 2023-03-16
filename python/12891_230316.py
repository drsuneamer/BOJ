# [BOJ] 12891. DNA 비밀번호  2023-03-16

import sys
input = sys.stdin.readline

S, P = map(int, input().split())
s = input()
ans = 0

a, c, g, t = map(int, input().split())

st = s[:P]
D = {'A': st.count('A'), 'C': st.count('C'), 'G': st.count('G'), 'T': st.count('T')}

ans = 0

if D['A'] >= a and D['C'] >= c and D['G'] >= g and D['T'] >= t:
    ans += 1

for i in range(P, S):
    new = s[i]
    old = s[i - P]

    D[new] += 1
    D[old] -= 1
    
    if D['A'] >= a and D['C'] >= c and D['G'] >= g and D['T'] >= t:
        ans += 1
    
print(ans)