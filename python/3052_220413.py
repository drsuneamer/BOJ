# [BOJ] 3052. 나머지  2022-04-13

L = []

for _ in range(10):
    a = int(input())
    if a % 42 not in L:
        L.append(a % 42)

print(len(L))