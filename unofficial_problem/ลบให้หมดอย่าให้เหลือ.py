num = []
s = 0
while True:
    x = int(input())
    if (x<0):
        s = x
        break
    num.append(x) 
for i in num:
    print(i+s)