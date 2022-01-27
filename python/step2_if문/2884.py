# 알람 시계   2022-01-27

hour, minute = map(int, input().split())

if minute >= 45:
    print(hour, minute - 45)
else:
    if hour == 0:
        print(23, minute + 15)
    else:
        print(hour - 1, minute + 15)



# 이건 왜 안될까?
H, M = map(int, input().split())

if H == 0:
    if M >= 45:
        print(23, M - 45)
    else:
        print(23, M + 15)
else:
    if M >= 45:
        print(H, M - 45)
    else:
        print(H - 1, M + 15)