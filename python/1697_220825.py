# [BOJ] 1697. 숨바꼭질
from collections import deque

def bfs():
    while q:
        a = q.popleft()

        if a == K:
            print(M[a])
            break

        else:
            for i in (a - 1, a + 1, a * 2):
                if 0 <= i <= m and M[i] == 0:
                    M[i] = M[a] + 1
                    q.append(i)

N, K = map(int, input().split())    # N: 수빈이의 위치, K: 동생의 위치
m = 100000
M = [0] * (m + 1)


q = deque()
q.append(N)

bfs()