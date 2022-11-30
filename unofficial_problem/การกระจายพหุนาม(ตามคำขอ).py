from math import *
def p(a, b):
    ans = pow(a, 2) + (2 * a * b) + pow(b, 2)
    print(int(ans))
def d(a, b):
    ans = pow(a, 2) - (2 * a * b) + pow(b, 2)
    print(int(ans))
n1 = int(input())
n2 = int(input())
p(n1,n2)
d(n1,n2)