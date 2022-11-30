n = list(map(int,input().split(':')))
name = input()
if n[0] > 5 and n[0] < 12:
    print('Good morning, {}'.format(name))
elif n[0] > 11 and n[0] < 18:
    print('Good afternoon, {}'.format(name))
else:
    print('Good evening, {}'.format(name))