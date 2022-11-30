import re
n = input()
s = 0
txt = re.findall('[A-Z][a-z]?|[0-9]+', n)
for i in txt:
    if i.isdigit():
        s+=int(i)
print('{:04d}'.format(s))