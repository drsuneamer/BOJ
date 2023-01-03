# [BOJ] 7369. Maya Calendar  2022-12-29

'''
Haab: 365일 1년, 19달
첫 18개월은 20일
(달의 이름들)
pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu
날짜는 이름 대신 0에서 19까지의 숫자로 표현
마지막 달의 이름은 uayet, 0에서 4까지 5일의 숫자로 표현
마지막 달은 unlucky한 달

Tzolkin - holly year
20일의 길이를 가진 13개의 기간
각각의 날짜는 숫자와 이름으로 이루어져 있음
(20개의 이름)
imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau
숫자는 1에서 13까지 반복

Haab 날짜를 Tzolkin 날짜로 바꾸는 로직 작성
'''

import sys

N = int(sys.stdin.readline())
h_month = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu']

t_month = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']

print(N)
for tc in range(N):
    d, m, y = sys.stdin.readline().split()
    date = int(y) * 365 + int(d[:-1])

    if m != 'uayet':
        date += h_month.index(m) * 20
    else:
        date += 18 * 20

    ans = [1, 'imix', 0]
    ans[0] = date % 13 + 1

    ans[2] = date // (20 * 13)
    # date %= 20 * 13

    ans[1] = t_month[date % 20]

    print(ans[0], ans[1], ans[2])