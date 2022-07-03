# [BOJ] 2501. 약수 구하기

N, K = map(int, input().split())    # N의 약수들 중 K번째로 작은 수 출력
ans = []

for i in range(1, N + 1):
    if N % i == 0:
        ans.append(i)

if K <= len(ans):
    print(ans[K-1])
else:
    print(0)