n = input()

if (n[len(n)-1] == 's' or n[len(n)-1] == 'x' or n[len(n)-1] == 'z' or (n[len(n)-2] == 's' and n[len(n)-1] == 'h') or (n[len(n)-2] == 'c' and n[len(n)-1] == 'h')):
    print(f'{n} -> {n}es')
elif(n[len(n)-1] == 'y'):
    y = n[:len(n)-1]
    print(f'{n} -> {y}ies')
else:
    print(f'{n} -> {n}s')

