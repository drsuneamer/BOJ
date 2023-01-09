# [BOJ] 15650. N과 M (2)


def sequence():
    if len(ans) == M:
        print(' '.join(ans))
        return
    else:
        for i in range(N):
            if L[i] not in ans:
                if len(ans) > 0:
                    if L[i] > int(ans[-1]):
                        ans.append(str(L[i]))
                        sequence()
                        ans.pop()
                else:
                    ans.append(str(L[i]))
                    sequence()
                    ans.pop()


N, M = map(int, input().split())
L = list(x for x in range(1, N + 1))
ans = []

sequence()
