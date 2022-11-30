data = list(map(str,input().split(' : ')))
police = list(map(str,input().split(' : ')))

if (data[1] == police[1] and data[0] == police[0]):
    print('T')
elif (data[0] != police[0] and data[1] != police[1]):
    print('DS')
else:
    print('F')