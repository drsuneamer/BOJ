# X보다 작은 수  2022-01-27

n, a = map(int, input().split())
numbers = map(int, input().split())

for num in numbers:
    if int(num) < a:
        print (num, end = ' ')
    