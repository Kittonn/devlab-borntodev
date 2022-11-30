data = {"w":'^',"a":"<","s":"v","d":">"}
c = []

for i in range(4):
    c.append(input())
for i in c:
    for j in data:
        if i == j:
            print(data[j])
