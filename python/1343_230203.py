# [BOJ] 1343. 폴리오미노

X = input()
ans = ''
cnt = 0

for x in X:
    if x == 'X':
        cnt += 1

    else:
        if cnt != 0:
            if cnt % 2:
                ans = -1
                # print(-1)
                break
            else:
                ans += 'AAAA' * (cnt // 4)
                ans += 'B' * (cnt % 4)
        ans += '.'
        cnt = 0

if cnt != 0 and ans != -1:
    if cnt % 2:
        ans = -1
    else:
        ans += 'AAAA' * (cnt // 4)
        ans += 'B' * (cnt % 4)

print(ans)