# [BOJ] <S3> 9742. 순열


def perm(r):
    global cnt
    if r == len(a):
        cnt += 1
        if cnt == int(b):
            print(''.join(selected))
            return

    for i in range(len(a)):
        if visited[i]:
            continue
        selected[r] = a[i]
        visited[i] = True
        perm(r + 1)
        visited[i] = False


while 1:
    try:
        a, b = input().split()
        selected = [''] * len(a)
        visited = [0] * len(a)
        cnt = 0

        maximum = 1
        for i in range(1, len(a) + 1):
            maximum *= i

        if int(b) > maximum:
            print(a, b,  '= No permutation')
        else:
            print(a, b, "= ", end="")
            perm(0)

    except:
        break
