n,x = map(int,input().split())
num = list(map(int,input().split()))
s = 0
for i in num:
    y = i * (x /100)
    if y % 1 >= 0.0001 and y % 1 < 1:
        y = (y // 1) + 1
    s+=y
print(int(s+sum(num)))