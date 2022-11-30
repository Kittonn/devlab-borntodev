n = int(input())
li = []
for i in range(n):
    x = int(input())
    li.append(x)
li.sort(reverse=True)
for i in li:
    print(i)