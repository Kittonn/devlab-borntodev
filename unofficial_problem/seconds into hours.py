n = int(input())
h = n // 3600
m = (n - (h * 3600)) // 60
s = (n - ((h * 3600) + (m * 60))) % 3600
print('{:d}:{:02d}:{:02d}'.format(h,m,s))
