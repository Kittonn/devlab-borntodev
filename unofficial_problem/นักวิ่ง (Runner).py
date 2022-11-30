x1,x2 = map(int,input().split())
v1,v2 = map(int,input().split())
i = 1
while True:
    if (i * v1) +x1 >= (i*v2)+x2:
        print(i)
        break
    i+=1