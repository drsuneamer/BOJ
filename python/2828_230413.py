import sys
input = sys.stdin.readline

N, M = map(int, input().split())
j = int(input())  # 사과의 개수

start = 1
end = M
ans = 0

for i in range(j):
    cur = int(input())
    if cur < start:
        g = abs(cur - start)
        ans += g
        start = cur
        end -= g
        
    elif cur > end:
        g = abs(cur - end)
        ans += g
        end = cur
        start += g

print(ans)
    
        
