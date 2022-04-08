from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        i = q.popleft()
        for j in computers[i]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1
    return visited


N = int(input())    # 컴퓨터의 수
M = int(input())    # 간선의 수
computers = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [0] * (N + 1)
bfs(1)
print(visited.count(1) - 1)     # 방문한 곳 개수 출력 (시작 지점 1 제외)