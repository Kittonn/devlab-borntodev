#price = kw * t * 3
t = []
for i in range(3):
    t.append(int(list(map(str,input().split(':'))).pop(1)))
def price(t):
    kw = [0.12,0.5,0.06]
    s = 0
    for i in range(len(t)):
        s += (kw[i] * 3 * t[i])
    return s
print('{:.2f}'.format(price(t)))