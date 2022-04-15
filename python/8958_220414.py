T = int(input())
for _ in range(1, T + 1):
    L = list(input())
    ans = 0
    score = 0
    for l in L:
        if l == 'O':
            score += 1
            ans += score
        else:
            score = 0
    print(ans)