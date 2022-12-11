# [BOJ] 17219. 비밀번호 찾기
import sys

# N: 저장된 주소의 수, M: 비밀번호를 찾으려는 주소의 수
N, M = map(int, sys.stdin.readline().split())
NL = {}

for _ in range(N):
    l = list(sys.stdin.readline().rstrip().split())
    NL[l[0]] = l[1]

for _ in range(M):
    print(NL[sys.stdin.readline().strip()])