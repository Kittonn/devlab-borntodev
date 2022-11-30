n = int(input())
if n>100:
    print('Error : Value must be less than or equal to 100.')
elif n<0:
    print('Error : Value must be greater than or equal to 0.')
elif n>=90:
    print('A')
elif n >= 85:
    print('B+')
elif n >= 80:
    print('B')
elif n >= 75:
    print('C+')
elif n >= 70:
    print('C')
elif n >= 65:
    print('D+')
elif n>=60:
    print('D')
elif n < 60:
    print('F')