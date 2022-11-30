data = ["st","nd","rd",'th','th']
n = [];new=[]
while True:
    x = input()
    if x == '-':
        break
    n.append(int(x))
    n.sort()
for i in n:new.append(str(i)+data[i-1])
for i in range(len(n)):
    if n[i] < 1 or n[i] > 5:
        print('Error! Not have this floor')
        break
    
    else:
        if i == 0:
            print('''OK! Wait please
---------------
Lift is arriving!''')
        print('''---------------
Lift is going up!
---------------
Lift has reached the {} floor!'''.format(new[i]))
        
