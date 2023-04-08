# [BOJ] <G5> 13023. ABCDE

import sys
input = sys.stdin.readline


def relate(i, r):
    """
    5명까지 갈 수 있는 경우가 잇는지 찾는 함수
    :param i: 현재 순회하고 있는 인덱스
    :param r: 현재 몇 명까지 카운트했는지
    :return: 가능한 경우를 찾으면 종료
    """
    global ans

    if r == 5:
        ans = 1
        return

    v[i] = 1
    for j in R[i]:
        if v[j] == 0:
            relate(j, r + 1)
    v[i] = 0


N, M = map(int, input().split())
R = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    R[a].append(b)
    R[b].append(a)

ans = 0

for i in range(N):
    v = [0] * N
    relate(i, 1)
    if ans == 1:
        break

print(ans)

