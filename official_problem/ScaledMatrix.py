#(num[index]-min(data)) / range
num= [];index = 0
m = int(input())
n = int(input())
for i in range(n*m):
    num.append(float(input()))
r = max(num)-min(num)
for i in range(n):
    for j in range(m):
        print('{:.4f}'.format((num[index]-min(num))/r),end= ' ')
        index += 1
    print()