num = int(input())
if (num <3):
    print('Box\'s height must be more than 2')
else:
    for i in range(num):
        print('#',end='')
    print('\r')
    for i in range(num-2):
        print('#',end='')
        for j in range(num-2):
            print(' ',end='')
        print('#',end='')
        print('\r')
    for i in range(num):
        print('#',end='')
