data1 = {'1':20,'2':30,'3':30,'4':40,'5':40};data2 = {'1':5,'2':10,'3':15,'4':20,'5':25};data3 = {'R':15,'B':15,'W':10,'G':15,'BK':15};data4 = {'1':20,'2':15,'3':25,'4':30,'5':25}
name1 = {'1':'underwear','2':'pants','3':'skirt','4':'shirt','5':'blouse'};name2 = {'1':'size S','2':'size M','3':'size L','4':'size XL','5':'size XXL'};name3 = {'R':'color red','B':'color blue','W':'color white','G':'color green','BK':'color black'};name4 = {'1':'cotton','2':'nylon','3':'spandex','4':'wool','5':'linen'}
data = []
for i in range(5):
    data.append(input())
ans=[data1[data[0]],data2[data[1]],data3[data[2]],data4[data[3]]]
name_ans = [name1[data[0]],name2[data[1]],name3[data[2]],name4[data[3]]]
for i in range(4):
    print(f'{name_ans[i]} - {ans[i]}')
    if i == 3:
        print('amount - {}\ncost - {}*{} = {}'.format(data[4],sum(ans),data[4],sum(ans)*int(data[4])))