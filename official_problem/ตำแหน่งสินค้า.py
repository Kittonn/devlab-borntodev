number = int(input())
m = []

for i in range(number):
    m.append(int(input()))
interest = int(input())

position = []

if interest not in m:
    print('Not Found')
else:
    for i in range(number):
        if m[i] == interest:
            position.append(str(i+1))
        else:
            pass

new_position = ','.join(position)
print('Position: '+new_position)

