# [BOJ] 1065. 한수  2022-04-19

N = input()
L = len(N)

if L <= 2:  # 2자리수까지는 모두 한수
    ans = N
else:
    ans = 99    # 3자리수부터는 99개의 한수 확보하고 시작
    for nn in range(100, int(N)+1):    # N까지 각 수 모두 확인
        n = str(nn)         # 인덱스 작업 위해 문자열로
        c = int(n[1]) - int(n[0])  # 두 수의 차이 (기준값)
        cnt = 0
        for i in range(2, len(n)):
            if int(n[i]) - int(n[i-1]) == c:    # 기준값과 각 자리별 차이 비교
                cnt += 1
            else:
                break
        if cnt == len(n) - 2:
            ans += 1

print(ans)

