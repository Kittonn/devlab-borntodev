txt = input()
li = list(map(str,txt.split()))
new = [];ti=[];ans=[]
for i in li:
    new.append(list(map(str,i.split('='))))
for i in range(len(new)):
    new[i].remove(new[i][0])
for i in range(len(new)):
    for j in range(len(new[i])):
        ti.append(list(map(str,new[i][j][1:-1].split(','))))
seta = set(ti[0]);setb = set(ti[1]);setc = set(ti[2])
setans = (seta.intersection(setb))-setc
j = ','.join(list(setans))
if len(j) == 0:
    print('none')
else:
    print(j)