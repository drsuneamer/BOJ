# [BOJ] 1978. 소수 찾기  2022-04-18

N = int(input())
L = list(map(int, input().split()))
ans = 0

for l in L:
    cnt = []
    for i in range(1, l + 1):   # 1부터 약수인지 찾기 시작
        if l % i == 0:
            cnt.append(i)   # 약수는 배열에 저장
    if len(cnt) == 2:   # 소수는 약수의 개수가 2
        ans += 1

print(ans)