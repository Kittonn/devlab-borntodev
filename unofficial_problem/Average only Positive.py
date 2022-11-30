num = []

while True:
    n = float(input())
    if n < 1:
        break
    num.append(n)
if (len(num) == 0):
    print('No Data')
else:
    print('{:.2f}'.format(sum(num)/len(num)))