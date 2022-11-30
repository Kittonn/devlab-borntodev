a,b,c,d,e,f = map(int,input().split())
A = a * c * e
B = (a * d * e) + (b * c * e) + (a * c * f)
C = (b * d * e) + (a * d * f) + (b * c * f)
D = b * d * f
print('{} {} {} {}'.format(A,B,C,D))