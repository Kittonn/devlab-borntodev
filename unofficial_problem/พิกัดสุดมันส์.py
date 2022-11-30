numtxt = input()
num = int(input())
x,y = map(int,numtxt[1:-1].split(','))
if x > num-1 or y > num-1:
    print('That position is not loaded.')
else:
    # แกน Y
    for i in range(num-1,-1,-1):
        #แกน X
        for j in range(num):
            #จุดพิกัด
            if i == y and j == x:
                print('*',end='')
            else:        
                print('#',end='')

        print('\r')