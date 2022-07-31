# [BOJ] 5635. 생일  2022-07-28
import sys

N = int(sys.stdin.readline())
S = [list(sys.stdin.readline().split()) for _ in range(N)]

SS = sorted(S, key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))

print(SS[0][0])
print(SS[-1][0])