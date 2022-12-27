# [BOJ] 11976. Promotion Counting  2022-12-17

L = list(list(map(int, input().split())) for _ in range(4))
ans = [0, 0, 0]

# 출력: 브->실, 실->골, 골->플 순서대로 출력 (정수 3개)
bef, aft = 0, 0
for i in range(4):
    bef += L[i][0]
    aft += L[i][1]

if aft > bef:
    L[0][0] += aft - bef

for i in range(3, -1, -1):
    if L[i][1] > L[i][0]:
        ans[i-1] = L[i][1] - L[i][0]
        L[i-1][1] += L[i][1] - L[i][0]

for a in ans:
    print(a)