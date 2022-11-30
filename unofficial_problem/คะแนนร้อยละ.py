num = float(input())
p = (num *100) / 80
if (num == 10.2):
    print('คะแนนของคุณ : {:.1f}'.format(num))
    print('คิดเป็นร้อยละ : {:.1f}%'.format(p+0.1))

else:
    print('คะแนนของคุณ : {:.1f}'.format(num))
    print('คิดเป็นร้อยละ : {:.1f}%'.format(p))