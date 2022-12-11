# [BOJ] 11866. 요세푸스 문제 0

N, K = map(int, input().split())
L = [n for n in range(1, N + 1)]
A = []  # 정답을 저장할 배열
c = 0

while len(L) > 0:
    c = c + K - 1
    l = len(L)
    while c >= l:
        c = c - l
    A.append(L.pop(c))

print('<', end='')
for a in range(len(A) - 1):
    print(A[a], end="")
    print(', ', end="")
print(A[-1], end="")
print('>')