# 빠른 A+B   2022-01-27

import sys

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)