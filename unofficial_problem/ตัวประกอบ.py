num = int(input())
ans = []
for i in range(1,num+1):
    for j in range(1,i+1):
        if i * j == num:
            ans.append(i)
            ans.append(j)

ans = sorted(set(ans))
txt = ','.join(str(i) for i in ans)
print('{} : {}'.format(len(ans),txt))