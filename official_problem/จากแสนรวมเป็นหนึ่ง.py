num = [int(i) for i in input()]
s = sum(num)

while len(str(s)) != 1:
    num = [int(i) for i in str(s)]
    s = sum(num)

print(s)