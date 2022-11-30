#txt = '01100010'
#txt_int = int(txt,2)
#print(chr(txt_int))


#= pu = 0 /////  pe = 1


txt = input()
ans = [];p =[];num=[];last = []
#for i in range(16,len(txt)+1,16):
#    ans.append(txt[i-16:i])
#print(ans)
#for i in ans:
for j in range(2,len(txt)+2,2):
    p.append(txt[j-2:j])
for i in range(8,len(p)+8,8):
    ans.append(p[i-8:i])
for i in range(len(ans)):
    n= []
    for j in range(len(ans[i])):
        if ans[i][j] == 'pe':
            n.append('1')
        if ans[i][j] == 'pu':
            n.append('0')
    num.append(n)



for i in num:
    txt = ''.join(i)
    txt = int(txt,2)
    last.append(chr(txt))
txt = ''.join(last)
print(txt)