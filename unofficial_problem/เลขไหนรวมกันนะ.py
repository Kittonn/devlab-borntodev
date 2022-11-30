#input()[1:-1]
txt = list(map(int,input()[1:-1].split(',')))
num = int(input())
s = 0;ans=[]
for i in range(1,len(txt)):
    for j in range(i+1):
        if txt[i] + txt[j] == num:
            ans.append(i)
            ans.append(j)

for i in range(1,len(ans),2):
    print(ans[i-1],ans[i])
        