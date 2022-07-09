# [BOJ] 10988. 팰린드롬인지 확인하기  2022-07-09

word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)