txt = list(input())
n = []
for i in range(1,len(txt)+1):
    if i % 2 == 0:
        x = txt[i-1].upper()
        n.append(x)
    else:
        n.append(txt[i-1])
for i in n:
    print(i,end='')