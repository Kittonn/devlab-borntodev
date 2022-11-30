i = int(input())
l = ['st','nd','rd','th','th']
if i > 5:
    print('Error! Not have this floor')
else:
    print('''OK! Wait please
---------------
Lift is arriving!
---------------
Lift is going up!
---------------
Lift has reached the {}{} floor!'''.format(i,l[i-1]))