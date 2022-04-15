C = int(input())
for _ in range(C):
    grades = list(map(int, input().split()))
    N = grades.pop(0)
    average = sum(grades) / N
    ans = 0

    for g in grades:
        if g > average:
            ans += 1

    print('{:.3f}%'.format(round(ans / N * 100, 3)))