from math import *
n = int(input())
new = sqrt(n)
if new % 1 == 0:
    print('Integer')
else:
    print('Float')