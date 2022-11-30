import re
molecule = input()
s = 0
ele = re.findall(r'[A-Z][a-z]*|\d+', re.sub('[A-Z][a-z]*(?![\da-z])', r'\g<0>1', molecule))
for i in ele:
    if i.isdigit():
        s+=int(i)
print(s)