t = int(input())
def height(t):
    return 0.5 * 9.8 * ((t/2) ** 2)
print('{:.2f}'.format(height(t)))