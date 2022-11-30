max=0;min=100
x = int(input())
y = int(input())
if x >y :
    max = x
    min = y
else:
    max = y
    min = x
print('MAX : '+str(max))
print('MIN : '+str(min))