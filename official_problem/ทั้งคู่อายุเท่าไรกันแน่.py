n,m,y = map(int,input().split())
ans = []
b = ((m-1)*y+n) / (m-1)
a = n+b
print(f'{int(a)} {int(b)}')