lucky = [8, 14, 112, 76, 2]
num = []
for i in range(5):
    num.append(int(input()))
s = 0
for i in num:
    for j in lucky:
        if i == j:
            s+=1
if s>=3:
    print('You are lucky')
else:
    print('You are unlucky')          