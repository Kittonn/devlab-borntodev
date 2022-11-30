s,y = map(int,input().split())
def len(s,y):
    return 1/((1/s)+(1/y))
if (len(s,y) > 0):
    print('{:.2f} cm'.format(len(s,y)))
    print('เลนส์นูน')
else:
    print('{:.2f} cm'.format(len(s,y)))
    print('เลนส์เว้า')