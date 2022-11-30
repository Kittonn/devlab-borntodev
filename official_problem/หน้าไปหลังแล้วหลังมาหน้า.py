n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
for i in range(n-1,-1,-1):
    print(num[i])