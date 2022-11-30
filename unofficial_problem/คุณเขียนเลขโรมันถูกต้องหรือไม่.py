n = input()
c = 0
for i in n:
    if i == 'I' or i == 'X':
        c+=1
    
if c>3:
    print('Not Correct')
else:
    print('Correct')