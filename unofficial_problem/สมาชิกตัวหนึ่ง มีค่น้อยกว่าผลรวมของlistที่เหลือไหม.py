txt = input()
n = list(map(int,txt[1:-1].split(',')))
b = "true"
for i in n:
    s = n.copy()
    s.remove(i)
    su = sum(s)
    if i > su:
        b = "false"
print(b)