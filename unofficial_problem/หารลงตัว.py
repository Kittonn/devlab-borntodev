new = list(map(int,input().split(',')))
ans = []
for i in new:
    if (i % 7 == 0 and i % 11 != 0) or (i == 1):
        ans.append(str(i))
x = ','.join(ans)
print(x)
