money = int(input())
kind = int(input())
angry = int(input())
steal = angry-kind
s = 0
for i in range(1,steal+1):
    s += i

if s > 1000 or s > money:
    print('Krit was arrested')
else:
    print(money-s)