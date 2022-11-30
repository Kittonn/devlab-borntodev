n = []
s = 0
num1 =int(input())
num2 = int(input())
for i in range(num1,num2+1):
    n.append(str(i))
for i in n:
    if '9' in i and i != "99":
        s+=1
    if i == '99':
        s+=2
print(s)