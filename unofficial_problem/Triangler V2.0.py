l = int(input())
h = int(input())
ans = (1/2)*l*h
if (ans % 1 == 0):
    print('{} cm2'.format(int(ans)))
else:
    print("{:.1f} cm2".format(ans))