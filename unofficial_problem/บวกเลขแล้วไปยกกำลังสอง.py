n = input()
n1 = input()
if n.isdigit() and n1.isdigit():
    print('{:,}'.format((int(n)+int(n1))**2))
else:
    print('Error')