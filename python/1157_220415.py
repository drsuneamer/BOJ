word = input()

dict = {}
for w in word.lower():
    if w in dict:
        dict[w] += 1
    else:
        dict[w] = 1

result = []
for d in dict.values():
    if d == max(dict.values()):
        result.append(d)

if len(result) > 1:
    print('?')
else:
    for k, v in dict.items():
        if v == max(dict.values()):
            print(k.upper())