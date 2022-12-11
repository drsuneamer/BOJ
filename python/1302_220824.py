# [BOJ] 1302. 베스트셀러
import sys

N = int(input())
books = {}

for n in range(N):
    a = input()
    if a in books:
        books[a] += 1
    else:
        books[a] = 1

m = 0
ans = ''
books = sorted(books.items())

for i in range(len(books)):
    if books[i][1] > m:
        m = books[i][1]
        ans = books[i][0]

print(ans)