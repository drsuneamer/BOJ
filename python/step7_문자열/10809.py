alp = 'abcdefghijklmnopqrstuvwxyz'
S = input()

for i in alp:
    if i in S:
        for j in range(len(S)):
            if i == S[j]:
                print(j, end=" ")
                break
    else:
        print(-1, end=" ")