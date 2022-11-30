n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

for i in num:
    if i % 105 == 0:
        print('YES')
    else:
        print('NO')