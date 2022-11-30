txt = [];s = 0;S=0;new=[]
data = {"P":1,"p":1,
        "N":3,"n":3,"B":3,"b":3,
        "R":5,"r":5,
        "Q":9,"q":9,
        "K":0,"k":0}
for i in range(8):
    txt.append(input().strip('.'))
for i in range(len(txt)):
    for j in txt[i]:
        if j != '.':
            new.append(j)
for i in new:
    if i != '':
        if i.isupper():
            S+=data[i]
        else:
            s+=data[i]
if (S-s) == 0:
    print('equal')
else:
    print(S-s)