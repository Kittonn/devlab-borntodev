txt = input()
txt = list(map(str,txt.split()))
A = set();B=set();C=set()
a = txt.index('A:')
b = txt.index('B:')
c = txt.index('C:')
for i in txt[a+1:b]:
    A.add(i)
for i in txt[b+1:c]:
    B.add(i)
for i in txt[c+1:]:
    C.add(i)
if len(A) > len(B) and len(A) > len(C):
    print('A')
elif len(B) > len(A) and len(B) > len(C):
    print('A')
else:
    print('C')