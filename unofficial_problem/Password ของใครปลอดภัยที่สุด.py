txt = input()
n = list(map(str,txt.split(',')))
dic = {'Man':n[0],'Non':n[1],'Miv':n[2]}
up=0;lo=0;num=0;sym=0;name=list(dic)
char = '#$@';ans={};M=[]
for j in dic:
    up=0;lo=0;num=0;sym=0
    for i in dic[j]:
        if i>='a'and i<='z':lo+=1
        if i>='A'and i<='Z':up+=1
        if i>='0'and i<='9':num+=1
        if i in char:sym+=1 
    if lo == 0 or num == 0 or up == 0 or sym == 0:    
        continue
    ans[j] = [lo,num,up,sym]
for i in ans:
    M.append(sum(ans[i]))
for i in range(len(n)):
    if len(n[i]) == max(M):
        print('{} ({})'.format(n[i],name[i]))
        break