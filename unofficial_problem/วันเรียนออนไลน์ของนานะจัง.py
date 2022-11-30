txt = input()
act = ['study math online', 'learn English online', 'learn Thai online', 'study science online', 'read test preparation o-net', 'do housework', 'learn to draw', 'learn to sing']
s = txt.split(',')
for i in s:
    if i in act:
        act.remove(i)
print('There is still {} things to do.'.format(len(act)))
for i in act:
    print('- {}'.format(i))

