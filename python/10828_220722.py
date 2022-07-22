# [BOJ] 10828. 스택
import sys

N = int(sys.stdin.readline())    # 주어지는 명령의 수
stack = [0] * N
top = -1

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        top += 1
        stack[top] = order[1]
    elif order[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif order[0] == 'size':
        print(top + 1)
    elif order[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])