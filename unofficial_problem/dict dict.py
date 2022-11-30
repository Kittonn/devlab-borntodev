txt = list(map(int,input()[1:-1].split(', ')))
dic = {}
for i in txt:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

t = 'False'
for i in dic:
    if dic[i] >= 2:
        t = 'True'
        break
print(t)