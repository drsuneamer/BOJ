# [BOJ] 2635. 수 이어가기  2022-12-29
import sys

N = int(sys.stdin.readline())
ans = 0
ANS = []

for n in range(1, N + 1):
    a = 1
    A = [N, n]  # 배열에 주어진 수와 선택한 정수 입력하고 시작

    while A[-1] >= 0:
        A.append(A[-2] - A[-1])
        a += 1

    if a > ans:
        ans = a
        ANS = A

print(ans)
for a in ANS:
    if a >= 0:
        print(a, end=" ")