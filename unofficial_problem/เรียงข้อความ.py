txt = [] #'python','java','javascript'

for i in range(int(input())):
    x = input()
    txt.append(x)
    txt.append(len(x))
def convert(txt):
    dct = {txt[i]: txt[i+1] for i in range(0,len(txt),2)}
    return dct
sort_arr = sorted(convert(txt).items(),key=lambda x: x[1])
for i in sort_arr:
    print(i[0])