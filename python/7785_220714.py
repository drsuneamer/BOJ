# [BOJ] 7785. 회사에 있는 사람

N = int(input())
now = {}
for i in range(N):
    name, status = input().split()
    if status == 'enter':
        now[name] = 1
    else:   # leave인 경우
        if name in now:
            del now[name]

for n in sorted(now, reverse=True):
    print(n)