W = list(input())
nums = [[], [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
        ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z']]
ans = 0

for w in W:
    for j in range(2, 10):
        if w in nums[j]:
            ans += (j + 1)
            break
print(ans)