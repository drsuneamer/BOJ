# [BOJ] 2491. 수열  2023-03-10

N = int(input())
L = list(map(int, input().split()))

ans = 1
    
# 시작 포인트 찾기
s1, e1 = 0, 0   # 작아지는 경우
s2, e2 = 0, 0   # 커지는 경우

for i in range(N - 1):
    if L[i + 1] <= L[i]:
        s1, e1 = i, i + 1
        ans = 2
        break

for i in range(N - 1):
    if L[i + 1] >= L[i]:
        s2, e2 = i, i + 1
        ans = 2
        break

while s1 < N - 1 and e1 < N - 1:
    if L[e1 + 1] <= L[e1]:
        e1 += 1;
        if e1 == N - 1:
            n = e1 - s1 + 1
            if n > ans:
                ans = n
    else:
        n = e1 - s1 + 1
        if n > ans:
            ans = n
        s1 = e1 + 1
        e1 = e1 + 1
        
while s2 < N - 1 and e2 < N - 1:

    if L[e2 + 1] >= L[e2]:
        e2 += 1;
        if e2 == N - 1:
            n = e2 - s2 + 1
            if n > ans:
                ans = n
    else:
        n = e2 - s2 + 1
        if n > ans:
            ans = n
        s2 = e2 + 1
        e2 = e2 + 1
        
print(ans)
    