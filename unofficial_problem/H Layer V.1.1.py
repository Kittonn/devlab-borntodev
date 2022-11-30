txt1 = list(input().upper())
txt2 = input().upper()
if 'H' in txt1[0]:
    txt1.pop(0)

txt1 = ''.join(txt1)

space = len(txt1) + 3 + len(txt2)
print('| {} {} |'.format(txt1,txt2))
print('|{}|'.format('—'*space))
print('|{}|'.format(' '*space))