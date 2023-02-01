# [BOJ] 1517. 버블 소트  2023-01-31
import sys
read = sys.stdin.readline


def mergeSort(list, p, q):
    if p >= q:
        return

    mid = (p + q) // 2
    mergeSort(list, p, mid)
    mergeSort(list, mid + 1, q)
    merge(list, p, mid + 1, q)


def merge(list, left, right, end):
    global ans
    merged = []
    l, r = left, right

    while l < right and r <= end:
        if list[l] <= list[r]:
            merged.append(list[l])
            l += 1
    else:
        merged.append(list[r])
        r += 1
        ans += right - l

    while l < right:
        merged.append(list[l])
        l += 1
    while r <= end:
        merged.append(list[r])
        r += 1

    l = left
    for n in merged:
        list[l] = n
        l += 1


N = int(read())
L = list(map(int, read().split()))
ans = 0
mergeSort(L, 0, N - 1)
print(ans)