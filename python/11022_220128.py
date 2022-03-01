# A + B -8   2022-01-27

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    result = a + b

    print(f'Case #{test_case}: {a} + {b} = {result}')