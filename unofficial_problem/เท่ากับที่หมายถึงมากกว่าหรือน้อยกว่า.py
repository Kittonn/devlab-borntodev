n = input()
s = 0
for i in range(len(n)):
    if n[i] == '=':
        s = i
n1 = int(n[:s-1])
n2 = int(n[s+1:])

if (n1 > n2):
    print(n1)
else:
    print(n2)