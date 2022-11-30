a = list(input().encode('ascii'))

num = [i**len(a) for i in a]
s = sum(num)

while len(str(s)) != 1:
    num = [int(i) for i in str(s)]
    s = sum(num)

print(s)
