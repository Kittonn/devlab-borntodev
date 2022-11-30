n = list(input())
n.remove('[')
n.remove(']')
s = ''.join(n)
def fac(x):
    if x == 0:
        return 1
    else:
        return x * fac(x-1)
print('{}!:{}'.format(s,fac(int(s))))