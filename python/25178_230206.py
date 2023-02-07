# [BOJ] 25178. 두라무리 휴지

N = int(input())
s1 = input()
s2 = input()
ans = "YES"

if s1[0] != s2[0]:
    ans = "NO"
if s1[-1] != s2[-1]:
    ans = "NO"
a1 = []
a2 = []
for s in s1:
    a1.append(s)
for s in s2:
    a2.append(s)

if sorted(a1) != sorted(a2):
    ans = "NO"

vowels = ['a', 'e', 'i', 'o', 'u']
a3, a4 = [], []
for a in a1:
    if a not in vowels:
        a3.append(a)
for a in a2:
    if a not in vowels:
        a4.append(a)

if a3 != a4:
    ans = "NO"

print(ans)