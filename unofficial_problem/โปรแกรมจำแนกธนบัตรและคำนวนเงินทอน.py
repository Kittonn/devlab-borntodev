cost = int(input())
money = int(input())
change = money - cost
dic_money = {}

for i in range(6):
    b,c = map(int,input().split())
    if b not in dic_money:
        dic_money[b] = c
print('change: {}'.format(change))
if change >= 1000 and dic_money[1000] >= 1:
    b_1000 = change // 1000
    if b_1000 > dic_money[1000]:
        print('cash: 1000 amount: {}'.format(dic_money[1000]))
        change -= dic_money[1000]*1000
    else:
        print('cash: 1000 amount: {}'.format(b_1000))
        change -= b_1000*1000
    
if change >= 500 and dic_money[500] >= 1:
    b_500 = change // 500
    if b_500 > dic_money[500]:
        print('cash: 500 amount: {}'.format(dic_money[500]))
        change -= dic_money[500]*500
    else:
        print('cash: 500 amount: {}'.format(b_500))
        change -= b_500*500
    
if change >= 100 and dic_money[100] >= 1:
    b_100 = change // 100
    if b_100 > dic_money[100]:
        print('cash: 100 amount: {}'.format(dic_money[100]))
        change -= dic_money[100]*100
    else:
        print('cash: 100 amount: {}'.format(b_100))
        change -= b_100*100
    
   
if change >= 50 and dic_money[50] >= 1:
    b_50 = change // 50
    if b_50 > dic_money[50]:
        print('cash: 50 amount: {}'.format(dic_money[50]))
        change -= dic_money[50]*50
    else:
        print('cash: 50 amount: {}'.format(b_50))
        change -= b_50*50
    
if change >= 20 and dic_money[20] >= 1:
    b_20 = change // 20
    if b_20 > dic_money[20]:
        print('cash: 20 amount: {}'.format(dic_money[20]))
        change -= dic_money[20]*20
    else:
        print('cash: 20 amount: {}'.format(b_20))
        change -= b_20*20
    
if change >= 10 and dic_money[10] >= 1:
    b_10 = change // 10
    if b_10 > dic_money[10]:
        print('cash: 5100 amount: {}'.format(dic_money[10]))
        change -= dic_money[10]*10
    else:
        print('cash: 10 amount: {}'.format(b_10))
        change -= b_10*10
    
    
