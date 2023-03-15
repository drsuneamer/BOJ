# [BOJ] 1759. 암호 만들기  2023-03-15

def combination(l, start):
    if l == L:
        v, c = 0, 0
        for s in selected:
            if s in vowels:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            print(''.join(selected))
        
        return
    
    for i in range(start, C):
        if visited[i] == True:
            continue
        
        selected[l] = lst[i]
        visited[i] = True
        combination(l + 1, i + 1)
        visited[i] = False
        
    
L, C = map(int, input().split())
lst = sorted(list(map(str, input().split())))

selected = [0] * L
visited = [0] * C
vowels = ['a', 'e', 'i', 'o', 'u']

combination(0, 0)