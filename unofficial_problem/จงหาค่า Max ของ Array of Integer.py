n = input()
l = list(map(int,n[1:len(n)-1].split(',')))
l.sort(reverse=True)
print(l[0])
