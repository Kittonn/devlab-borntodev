num = []
while True:
    x = int(input())
    if (x < 1):
        break
    num.append(x)
print(sum(num) / len(num))