# [BOJ] 1966. 프린터 큐

T = int(input())
for tc in range(T):
    # N: 문서의 개수, M: 현재 queue에서의 위치
    N, M = map(int, input().split())
    ans = 0

    # N개 문서의 중요도
    imp = list(map(int, input().split()))
    L = ['o'] * N
    L[M] = 'x'

    while 'x' in L:
        # 맨 앞 값보다 중요도가 높은 값이 하나라도 있는 경우
        while imp[0] < max(imp):
            L.append(L.pop(0))
            imp.append(imp.pop(0))

        if imp[0] == max(imp):
            L.pop(0)
            imp.pop(0)
            ans += 1

    print(ans)



