txt=[];char = '@_!#$%^&*()<>?/\|}{~:[]\'\"';ans=[]
for i in range(3):
    txt.append(list(map(str,input().split(':'))))
dic = dict(txt)

data_g = list(map(str,dic['GUITAR'][1:-1].split(', ')))
for i in data_g:
    if any(j in char for j in i):
        pass
    else:
        ans.append(i)
t = ', '.join(ans)
print(f'GUITAR:[{t}]')