n=  int(input())
li = []
for i in range(n):
    li.append([])
for i in range(n):
    for j in range(3):
        x = input()
        li[i].append(x)
print('--Customers Information--')
for i in range(n):
    print(str(li[i][0])+' (age : '+str(2017-int(li[i][1]))+')')