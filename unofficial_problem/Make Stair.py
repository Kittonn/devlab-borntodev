h = '__'
v = '__|'
num = int(input())
if num == 0:
    print(h)
else:
    for i in range(num*3,-1,-3):
        if i == num*3:
            print(' '*i,end='')
            print(h)
        else:
            print(' '*i,end='')
            print(v)