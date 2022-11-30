n = int(input())
s = (n // 3) + (n%3)
n+= n //3

while s>=3:
    s //=3
    n+=s
    s += s% 3
print(n)    