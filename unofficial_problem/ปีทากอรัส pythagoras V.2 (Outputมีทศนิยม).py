from math import *
n1 = int(input())
n2 = int(input())
ans = sqrt(pow(n1, 2) + pow(n2, 2))
if (ans % 1 == 0):
    print(int(ans))
else:
    print('{:.2f}'.format(ans))