# [BOJ] 2822. 점수 계산  2022-07-15

scores = [0] * 8
for i in range(8):
    scores[i] = int(input())

new_scores = sorted(scores)
ans = 0
idxs = []
for i in range(1, 6):
    ans += new_scores[-i]
    for j in range(8):
        if new_scores[-i] == scores[j]:
            idxs.append(j + 1)

new_idxs = sorted(idxs)

print(ans)
for i in new_idxs:
    print(i, end=" ")