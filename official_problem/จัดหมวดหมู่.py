num = int(input())
data = []
for i in range(int(input())):
    data.append(list(map(str,input().split())))
for i in range(len(data)):
    if int(data[i][0]) <= num <= int(data[i][1]):
        print(data[i][2])