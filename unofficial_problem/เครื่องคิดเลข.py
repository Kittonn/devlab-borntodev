num = []
for i in range(3):
    num.append(input())
if (num[0] == '+'):
    print(int(num[1])+int(num[2]))
elif (num[0] == '-'):
    print(int(num[1])-int(num[2]))
elif (num[0] == '*'):
    print(int(num[1])*int(num[2]))
else:
    print(int(int(num[1])/int(num[2])))