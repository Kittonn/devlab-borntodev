txt = input().strip(' ')

if txt[-1] != ';' or txt[-2] != ')' or txt[6] != '(' or txt[:6] != "printf" or txt[7] != '"' or txt[-3] != '"':
    print('Compile Error!')
else:
    print(txt[8:-3])