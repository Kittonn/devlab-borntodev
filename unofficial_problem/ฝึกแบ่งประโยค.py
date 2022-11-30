txt = input()
sl = input()

li = list(map(str,txt.split(sl)))
if (' ' not in li):
    for i in range(len(li)):
        print(li[i],end='')
        if i == len(li) -1:
            break
        print(f'{sl}\n{sl}',end='')
else:
    for i in li:
        print(i,end='')
    if '.' not in i:
        print(f'{sl}\n{sl}',end='')