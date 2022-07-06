# [BOJ] 1259. 펠린드롬수  2022-07-06

while 1:
    s = input()
    if s == '0':
        break
    elif s == s[::-1]:
        print('yes')
    else:
        print('no')