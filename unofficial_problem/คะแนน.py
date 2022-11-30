g = ['fail', 'good', 'very good', 'excellent']
n = int(input())
if (n <= 100 and n >= 76):
    print(g[3])
elif (n <= 75 and n >= 51):
    print(g[2])
elif (n <= 50 and n >= 26):
    print(g[1])
else:
    print(g[0])