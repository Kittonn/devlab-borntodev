r = int(input())
p = int(input())
total = 0
for i in range(1,r+1):
    print('{}-{}'.format(i,p))
    total += p
print(total)