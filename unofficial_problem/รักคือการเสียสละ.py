n = input()
c = []
v = []
for ch in n:
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        v.append(ch)
    elif(ch == ' ' or ch == '.' or ch == '!' or ch == '#' or ch == '@' or ch == ','):
        pass
    else:
        c.append(ch)
for i in v:
    print(i, end = '')    
print('\r')
for i in c:
    print(i, end = '') 
