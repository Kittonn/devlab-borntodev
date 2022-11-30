txt = ['Thin', 'Good Health', 'Fat Level 1', 'Fat Level 2', 'Fat Level 3']
w = int(input())
h = int(input())
a = ''
def bmi(x, y):
    b = x / (pow(y / 100, 2))
    return b
b = bmi(w, h)
print('{:.2f}'.format(b))
if (b > 30):
    print(txt[4])
elif (b >= 25 and b <= 29):
    print(txt[3])
elif (b >= 23 and b <= 24):
    print(txt[2])
elif (b >= 18 and b <= 22):
    print(txt[1])
else:
    print(txt[0])