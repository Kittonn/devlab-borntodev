num = list(map(int,input().split()))
dis = []
for i in range(3):
    dis.append(int(input()))
num = [abs(i) for i in num]
num.sort()
for i in range(3):
    print('Distance{} = {}'.format(i+1,num[i] + dis[i]))
