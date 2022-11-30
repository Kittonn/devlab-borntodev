t = float(input())

def v(t):
    x = 40 / t
    return x

print('{:.2f} km/hr'.format((v(t)*18)/5))