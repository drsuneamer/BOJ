# [BOJ] 15649. N과 M  2023-01-05
import sys


def backtrack():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    else:
        for i in range(1, N + 1):
            if i not in ans:
                ans.append(i)
                backtrack()
                ans.pop()


N, M = map(int, sys.stdin.readline().split())
ans = []
backtrack()
