# [BOJ] 2476. 주사위 게임  2022-07-17

N = int(input())    # 참가자 수
ans = 0

for i in range(N):
    a, b, c = map(int, input().split())
    m = 0
    if a == b == c:
        m = 10000 + a * 1000
    elif a == b or b == c:
        m = 1000 + b * 100
    elif a == c:
        m = 1000 + a * 100
    else:
        m = max(a, b, c) * 100

    if m > ans:
        ans = m

print(ans)