ct= []
for i in range(int(input())*2):
    ct.append(input())
dic = {int(ct[i-1]):ct[i] for i in range(1,len(ct),2)}
for i in sorted(dic):
    print('Chapter {}'.format(i))
    print(dic[i])