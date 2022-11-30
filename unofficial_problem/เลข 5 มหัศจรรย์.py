from math import sqrt

n = int(input())
if (sqrt(n) % 1==0):
    print(int(sqrt(n)))
else:
    print('No Numbers Matching!')