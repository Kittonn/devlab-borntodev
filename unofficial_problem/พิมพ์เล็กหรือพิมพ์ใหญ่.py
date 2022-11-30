from string import *
txt = input()
sum_upper = 0
sum_lower = 0
for i in txt:
    if i in punctuation or i == ' ':
        pass
    else:
        if i == i.upper():
            sum_upper += 1
        if i == i.lower():
            sum_lower += 1
print('UPPER:{}'.format(sum_upper))
print('LOWER:{}'.format(sum_lower))