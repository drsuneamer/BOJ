# [BOJ] <S5> 1251. 단어 나누기


def comb(r, start):
    global ans
    if r == 2:
        a = s[:selected[0]]
        b = s[selected[0]:selected[1]]
        c = s[selected[1]:l]
        t = a[::-1] + b[::-1] + c[::-1]
        ans = min(t, ans)
        return

    for i in range(start, len(idx)):
        if visited[i]:
            continue
        selected[r] = idx[i]
        visited[i] = 1
        comb(r + 1, i + 1)
        visited[i] = 0


s = input()
l = len(s)

ans = 'z' * l

idx = [x for x in range(1, l)]
selected = [0] * 2
visited = [0] * len(idx)


comb(0, 0)
print(ans)
