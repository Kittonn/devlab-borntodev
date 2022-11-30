n = input()
new = []
for ch in n:
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        pass
    else:
        new.append(ch)
for i in new:
    print(i, end = '')
