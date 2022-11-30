#v^2 = u^2 + 2gs
from math import pow, sqrt
def d(s):
    v = sqrt(20*s)
    return v
n = int(input())
print('{:.2f} m/s'.format(d(n)))