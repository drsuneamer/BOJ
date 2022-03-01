# 최소, 최대  2022-02-06

N = int(input())
numbers = list(map(int, input().split()))
min_num = numbers[0]
max_num = numbers[0]

for n in numbers:
    if n < min_num:
        min_num = n

for n in numbers:
    if n > max_num:
        max_num = n

print(min_num, end = ' ')
print(max_num)