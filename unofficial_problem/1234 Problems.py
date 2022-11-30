n,m,k,a = map(int,input().split())
s = 0

for i in range((m-n)+1):
    s+= (k + a*i)
if (1234 - s <= 0):
    print('YES')
else:
    print(1234-s)