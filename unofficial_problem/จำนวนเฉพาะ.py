prime = []
num = int(input())
for i in range(2,num+1):
    p = True
    for j in range(2,i):
        if (i % j == 0):
            p = False
    if p:
        prime.append(i)
        
if len(prime) != 0:
    print(f'จำนวนเฉพาะในช่วง 0 ถึง {num}\nมีอยู่ {len(prime)} จำนวน')
    
else:
    print('ไม่สามารถหาได้')
    
    
        