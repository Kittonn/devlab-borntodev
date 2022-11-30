data = {'Dog': 4, 'Cat': 4, 'Chicken':2, 'Duck': 2, 'Cow':4,'Snake':0,'Bird':2}
li = dict(input().split() for i in range(3))

s = 0
for i in data:
    for j in li:
        if i == j:
            s += (data[i] * int(li[j]))
print(s)