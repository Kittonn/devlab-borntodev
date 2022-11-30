txt = input()
if txt == 'Fire':
    print('{0:020b}'.format(0))
elif txt == 'Water':
    print('{0:020b}'.format(1))
elif txt == 'Wind':
    print('{0:020b}'.format(2))
elif txt == 'Ground':
    print('{0:020b}'.format(3))
elif txt == 'Light':
    print('{0:020b}'.format(4))
elif txt == 'Dark':
    print('{0:020b}'.format(5))
else:
    print('No have this mahou in your library.')