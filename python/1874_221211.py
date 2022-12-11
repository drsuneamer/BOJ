# [BOJ] 1874. 스택 수열

n = int(input())
L = list(int(input()) for _ in range(n))
stack = []
ans = []
k = 1
tf = 'YES'

while tf == 'YES' and k <= n:
    for i in range(n):
        # 현재 사용 가능한 값보다 큰 값을 출력해야 하면
        if L[i] >= k:
            # stack[top]과 같아질 때까지 push
            if len(stack) == 0:
                stack.append(k)
                ans.append('+')
                k += 1
            while stack[-1] != L[i]:
                stack.append(k)
                ans.append('+')
                k += 1
            if stack[-1] == L[i]:
                stack.pop(-1)
                ans.append('-')
        else:
            if L[i] == stack[-1]:
                stack.pop(-1)
                ans.append('-')
            else:
                tf = 'NO'
                break

if tf == 'NO':
    print(tf)
else:
    for a in ans:
        print(a)
