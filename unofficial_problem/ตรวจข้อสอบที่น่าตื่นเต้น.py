n,k,m,p=map(int,input().split())
correct = input()
select = input()
s = 0
for i in range(len(select)):
    if select[i] != correct[i] and select[i] != 'X':
        s-=m
    if select[i] == 'X':
        s+=p
    if select[i] == correct[i]:
        s+=k  
print(f'Your score:{s}')