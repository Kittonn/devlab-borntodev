num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
s = []
if(len(num1) != len(num2) or sum(num1) > 32548 or sum(num2) > 32548):
    print("Invalid")
else:
    for i in range(len(num1)):
        s.append(num1[i] + num2[i])
    for i in s:    
        print(i, end = ' ')
    