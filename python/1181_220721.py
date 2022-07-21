# [BOJ] 1181. 단어 정렬

N = int(input())    # 단어의 개수
L = [0] * N

for i in range(N):
    L[i] = input()

for x in (sorted(set(L), key=lambda x: (len(x), x))):
    print(x)