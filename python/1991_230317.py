# [BOJ] <S1> 1991. 트리 순회

def pre(n):
    if n == -19:
        return;
    print(chr(n + 65), end="")
    pre(L[n][0])
    pre(L[n][1])


def inorder(n):
    if n == -19:
        return;
    inorder(L[n][0])
    print(chr(n + 65), end="")
    inorder(L[n][1])


def post(n):
    if n == -19:
        return;
    post(L[n][0])
    post(L[n][1])
    print(chr(n + 65), end="")


N = int(input())
L = [[] for _ in range(N)]

for _ in range(N):
    a, b, c = input().split()
    L[ord(a) - 65].append(ord(b) - 65)
    L[ord(a) - 65].append(ord(c) - 65)

pre(0)
print()
inorder(0)
print()
post(0)
