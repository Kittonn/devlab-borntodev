n,r = map(int,input().split())
for i in range(0,r):
    print('{}{}{}'.format('-'*(r-i),'*'*(n-((r-i)*2)),'-'*(r-i)))
for i in range(n-(r*2)):
    print('*'*n)
for i in range(r-1,-1,-1):
    print('{}{}{}'.format('-'*(r-i),'*'*(n-((r-i)*2)),'-'*(r-i)))