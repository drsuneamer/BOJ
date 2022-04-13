# [BOJ] 1244. 스위치 켜고 끄기  2022-04-13

N = int(input())    # 스위치 개수
switch = [9] + list(map(int, input().split()))    # 1:ON, 2: OFF
S = int(input())    # 학생 수

for _ in range(S):
    a, b = map(int, input().split())    # a: 성별, b: 받은 스위치 번호
    if a == 1:  # 남학생의 경우 - 배수
        for j in range(1, N + 1):   # 스위치 번호 - 1부터 N까지
            if j % b == 0:
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1
    else:       # 여학생의 경우 - 대칭
        d = 0
        for j in range(1, (N + 1) // 2):   # 스위치부터의 거리
            if 1 <= b - j <= N and 1 <= b + j <= N:  # 스위치 범위 내에 있으면
                if switch[b - j] == switch[b + j]:
                    d += 1
                else:
                    break
            else:
                break
        for j in range(b - d, b + d + 1):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0

for i in range(1, N+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()

