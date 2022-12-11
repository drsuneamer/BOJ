# [BOJ] 18111. 마인크래프트
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())     # 세로 N, 가로 M, 인벤토리 B
G = [list(map(int, input().split())) for _ in range(N)]

print(max(map(max, G)))

