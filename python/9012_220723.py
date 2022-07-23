# [BOJ] 9012. 괄호  2022-07-23

N = int(input())

for _ in range(N):
    l = input()
    ans = ""
    top = -1
    for i in range(len(l)):
        if l[i] == '(':
            top += 1
        else:
            if top <= -1:
                ans = "NO"
                top -= 1
                break
            else:
                top -= 1

    if top == -1:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)