n = input()
ans = []
for i in n:
    if i == i.upper():
        ans.append(i.lower())
    else:
        ans.append(i.upper())
for i in ans:
    print(i, end = '')