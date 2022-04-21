N = int(input())
ans = N     # 모두 그룹단어라는 가정하에 시작
for _ in range(N):
    L = []
    S = input()
    for i in range(len(S)):
        if S[i] not in L:   # 이전에 나온 문자인지 체크
            L.append(S[i])
        elif S[i-1] != S[i]:    # 이전에 나온 문자인데 앞 글자와 다르면
            ans -= 1        # 그룹 단어 개수 - 1
            break

print(ans)