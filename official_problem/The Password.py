txt = list(input())
char = '@_!#$%^&*()<>?/\|}{~:[]\'\"'
up=0;lo=0;num=0;sym=0
for i in txt:
    if i>='a'and i<='z':lo+=1
    if i>='A'and i<='Z':up+=1
    if i>='0'and i<='9':num+=1
    if i in char:sym+=1  
if  len(txt) <=20 and len(txt) >= 3:
    if up > 0 and lo > 0 and num > 0 and sym > 0:
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')