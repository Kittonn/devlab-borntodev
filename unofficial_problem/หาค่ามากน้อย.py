x = 1
m = 10000000000
M = -10000000000
c = 0
while x != 0:
    x = int(input())
    if x == 0:
        break
    else:
        if x > M:
            M = x
        if x < m:
            m = x
        c += 1
if x == 0 and c == 0:
    print('Total : {}'.format(0))
    print('Maximum : {}'.format(0))
    print('Minimum : {}'.format(0))
else:    
    print('Total : {}'.format(c))
    print('Maximum : {}'.format(M))
    print('Minimum : {}'.format(m))    

