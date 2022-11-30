from math import sqrt
num = int(input())

if (num == -1):
    print('i')
elif (num <0):
    print('false')
elif (sqrt(num)%1 ==0):
    print(int(sqrt(num)))
else:
    print('false')