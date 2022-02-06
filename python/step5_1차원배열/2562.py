# 최댓값  2022-02-06

max_num = 0
which_num = 0 

for i in range(1, 10):
    n = int(input())
    if n > max_num:
        max_num = n
        which_num = i
    
print(max_num)
print(which_num)