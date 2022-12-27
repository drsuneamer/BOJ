# [BOJ] 10420. 기념일 1  2022-12-19
from datetime import datetime
from datetime import timedelta

N = int(input())

date = datetime.strptime('2014-04-01', '%Y-%m-%d')
ans = date + timedelta(days=N)

print(str(ans)[:10])