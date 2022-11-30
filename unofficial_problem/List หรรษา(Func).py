x = input()
li = list(map(int,x[1:len(x)-1].split(',')))

ans = []
s = 0
for i in range(len(li)):
    s += li[i]
    ans.append(str(s))
x = ', '.join(ans)
print(f'[{x}]')