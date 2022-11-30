n = int(input());s = 0
for i in range(1,n+1):
    if i == n:
        print('{}/{}\\'.format(' '*(n-i),'_'*s),end='')
        break
    print('{}/{}\\'.format(' '*(n-i),' '*s),end='')
    s+=2
    print('\r')