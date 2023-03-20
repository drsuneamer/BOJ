# [BOJ] <S2> 11725. 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6)	# 안하면 recursionError
input = sys.stdin.readline

def search(v):
    visited[v] = True
    for n in tree[v]:
        if visited[n] == False:	# 아직 탐색하지 않은 값이 있다면 자식에 해당
            ans[n] = v
            search(n)
    return

            
N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
ans = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

search(1)	# 문제 조건: 노드는 1
for i in range(2, N + 1):
    print(ans[i])
