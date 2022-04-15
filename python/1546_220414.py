N = int(input())
grade = list(map(int, input().split()))
M = max(grade)
result = []
for g in grade:
    result.append(g/M*100)

print(sum(result)/N)