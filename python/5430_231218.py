# [BOJ] 5430. AC

import sys

input = sys.stdin.readline

T = int(input())  # T <= 100

# R: 뒤집기, D: 첫번째 버리기
for tc in range(T):
    P = input().rstrip()
    L = int(input())
    a = input().rstrip()[1:-1].split(',')
    arr = []
    for aa in a:
        try:
            arr.append(int(aa))
        except:
            pass

    d = 1
    tf = 1
  
    for p in P:
        if p == 'R':  # R인 경우 방향만 바꿈
            d = abs(d - 1)
    
        else:  # D인 경우 pop
            try:
                if d == 1:
                    arr.pop(0)
                else:
                    arr.pop(-1)
            except:
                tf = 0
                break
    
    if tf == 1:
        if d == 0:
            arr.reverse()
        print('[', end="")
        for a in arr[:-1]:
            print(a, end=",")
        try:
            print(arr[-1], end="")
        except:
            pass
        print("]")
    else:
        print('error')
