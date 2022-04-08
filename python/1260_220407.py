def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in arr[v]:
        if visited[i] == 0:
            dfs(i)

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        i = q.pop(0)
        print(i, end=" ")
        for j in arr[i]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1

N, M, V = map(int, input().split())
arr = [list() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


for i in range(N + 1):
    arr[i].sort()


visited = [0] * (N + 1)
dfs(V)

print()

visited = [0] * (N + 1)
bfs(V)