n = int(input())
if n <=0:
    print("Input must be greater than 0.")
else:
    for i in range(1,n+1):
        for j in range(i):
            if i % 2 == 0:
                print('2',end='')
            else:
                print('5',end='')
        print('\r')