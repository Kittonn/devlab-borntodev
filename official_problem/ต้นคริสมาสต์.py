n = int(input())
for i in range(n):
    for j in range(1,i+3):
        for k in range(n-j+1):
            print(' ',end='')
        for m in range(j*2-1):
            print('*',end='')
        print()

print('{}|'.format(' '*n))
print('{}V{}'.format('='*n,'='*n))