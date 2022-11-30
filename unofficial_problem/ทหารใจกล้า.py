a = list(input().encode('ascii'))
ans=[];new=[]
for i in range(1,len(a)+1):
    x = a[i-1]-i
    ans.append(x)
n = ''.join(chr(i) for i in ans)
for i in n:
    if i.isupper():
        new.append(i.lower())
    else:
        new.append(i.upper())
x = ''.join(new)
print(x)