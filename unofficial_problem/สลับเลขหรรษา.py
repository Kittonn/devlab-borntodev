num = []
for i in range(3):
    num.append(''.join(reversed(input())))
print('{} + {} = {}'.format(num[0], num[2], int(num[0]) + int(num[2])))