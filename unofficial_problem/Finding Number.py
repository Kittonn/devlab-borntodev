n = int(input())
num = list(map(int, input().split()))
find = int(input())

if find in num:
    print('Yes')
else:
    print('No')