n = int(input())
if n % 2 != 0:
    n -= 1
s = 0
for i in range(2, n+2, 2):
    s += (i ** 2)
print(s)