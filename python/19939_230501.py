# [BOJ] <S4> 박 터뜨리기
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
fn = 0

for i in range(1, K + 1):
    fn += i

if fn > N:  # 나눠 담을 수 없는 경우
    print(-1)
else:
    N -= fn
    if N % K == 0:
        print(K - 1)
    else:
        print(K)
    
