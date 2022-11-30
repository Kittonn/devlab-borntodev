data = [];dic={};M=0
for i in range(4):
    data.append(input().lower())
for i in data:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1
#new = {dic[i]:i for i in dic}
for i in sorted(dic):
    if dic[i] == max(dic.values()):
        print(i.capitalize())
        break
    if max(dic.values()) == min(dic.values()):
        print(data[3].capitalize())
        break