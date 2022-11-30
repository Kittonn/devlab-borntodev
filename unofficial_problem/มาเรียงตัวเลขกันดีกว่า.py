num = list(map(str,input().split()))
n = [];new = []
for i in range(int(num[1])):
    n.append(int(input()))

for i in range(len(n)):
    new.append(n[i])
    new.sort()
    x = ', '.join(str(i) for i in new)
    print("ROW {} : [{}]".format(i+1,x))