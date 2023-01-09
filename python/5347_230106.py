# [BOJ] 5347. LCM
import sys

T = int(sys.stdin.readline())
for tc in range(T):
    a, b = map(int, sys.stdin.readline().split())
    k = max(a, b)
    while 1:
        if k % a == 0 and k % b == 0:
            print(k)
            break
        else:
            k += max(a, b)