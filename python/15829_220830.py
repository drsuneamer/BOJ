# [BOJ] 15829. Hashing

N = int(input())
S = input()
ans = 0
for i in range(N):
    ans += (ord(S[i])- 96) * (31 ** i)

print(ans % 1234567891)