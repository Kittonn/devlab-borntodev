data = ["Red","Yellow","Blue","White"]
n=[];s=0;ans=[]
for i in range(3):
    x = input()
    if x == 'Blue':
        s += 1
    n.append(x)
for i in n:
    if i not in data:
        ans.append('ERROR')
        break
if 'Red' not in n:
    ans.append('Second Line')
elif n[2] == 'White':
    ans.append('Third Line')
elif s > 1:
    ans.append('First Line')
else:
    ans.append('Third Line')
print(ans[0])
