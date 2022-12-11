import sys

N = int(sys.stdin.readline())

C = [0] * 10001

for i in range(N):
    C[int(sys.stdin.readline())] += 1

for i in range(len(C)):
    if C[i] != 0:
        for _ in range(C[i]):
            print(i)