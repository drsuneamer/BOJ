# [BOJ] 1158. 요세푸스 문제  2023-03-10

from collections import deque
N, K = map(int, input().split())

L = deque()
for i in range(1, N + 1):
    L.append(i)
    
ans = deque()

while len(L) > 0:
    for i in range(0, K - 1):
        L.append(L.popleft())
    ans.append(L.popleft())
    
print("<", end="")
for i in range(N - 1):
    print(ans[i], end="")
    print(", ", end="")
print(ans[-1], end="")
print(">")