# [BOJ] 12933. 오리  2023-03-09

S = input()

ans = 0
A = []
L = ['0', 'q', 'u', 'a', 'c', 'k']

for i in range(len(S)):
    s = S[i]
    if L.index(s) == 1:
        # q가 나온 경우
        t = 1
        for j in range(len(A)):
            if L.index(A[j][-1]) == 5:
                A[j] += s
                t = 0
                break
        if t == 1:
            A.append(s)
            
    else:
        t = 1
        for j in range(len(A)):
            if L.index(A[j][-1]) + 1 == L.index(s):
                t = 0
                A[j] += s
                break
        if t == 1:
            ans = -1
            break
    

for a in A:
    if a[-1] != 'k':
        ans = -1
        
if ans == -1:
    print(ans)
else:
    print(len(A))
            