n300 = int(input())
n100 = int(input())
n50 = int(input())
n0 = int(input())

def circle(n300,n100,n50,n0):
    return ((50 * n50) + (100 * n100) + (300 * n300)) / (300 * (n0 + n50 + n100 + n300))
print('{:.2f}%'.format(circle(n300,n100,n50,n0)*100))