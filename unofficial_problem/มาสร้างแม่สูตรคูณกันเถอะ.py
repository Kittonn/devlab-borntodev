n = int(input())
total = 0
for i in range(1,13):
    s = i * n
    total += s
    print('{} x {} = {}'.format(n, i, s))

print('รวม : {:,.2f}'.format(total))