num = int(input())
if (num==1):
    print('#')
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
