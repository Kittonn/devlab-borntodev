s = input()
s2 = list(map(int, s.split('+')))
s2.sort()
print('+'.join(str(e) for e in s2))