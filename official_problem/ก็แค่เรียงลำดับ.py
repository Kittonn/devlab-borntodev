li = []
for i in range(5):
    x = int(input())
    li.append(x)
li.sort(reverse=True)
for i in li:
    print(i)