x = 1 
n = []
while (x != 0):
    j = int(input())
    if (j == 0):
        break
    n.append(j)
txt = input()
if (txt == 'MaX'):
    n.sort(reverse = True)
else:
    n.sort()
for i in n:
    print(i, end = ' ')