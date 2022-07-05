# [BOJ] 2750. 수 정렬하기

def ins_sort(a):    # 삽입 정렬
    n = len(a)      # a: 정렬할 리스트
    for i in range(1, n):
        key = a[i]  # 비교할 인덱스의 값 저장해둠
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key



N = int(input())    # 수의 개수
arr = []

for i in range(N):
    arr.append(int(input()))    # 입력 받아서 리스트에 넣기

ins_sort(arr)
for a in arr:
    print(a)