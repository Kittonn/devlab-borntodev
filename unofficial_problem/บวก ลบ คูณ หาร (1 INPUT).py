p = list(map(str, input().split()))
total = 0
if (p[1] == '+'):
    total = int(p[0]) + int(p[2])
    print('{} {} {} = {}'.format(p[0], p[1], p[2], total))
elif (p[1] == '-'):
    total = int(p[0]) - int(p[2])
    print('{} {} {} = {}'.format(p[0], p[1], p[2], total))
elif (p[1] == '*'):
    total = int(p[0]) * int(p[2])
    print('{} {} {} = {}'.format(p[0], p[1], p[2], total))
else:
    total = int(p[0]) / int(p[2])
    print('{} {} {} = {}'.format(p[0], p[1], p[2], total))