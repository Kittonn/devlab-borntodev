month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
n = int(input())
c = 0
for i in range(1,month[n]+1):
    s = 0
    if i == 1:
        s = i+31
        if s % n == 0:
            c+=1
    else:
        s = i+(i-1)
        if s % n == 0:
            c+=1
print(c)