n = int(input())

def re(x):
    if x == 0:
        return 1
    elif (x < 0):
        return -1
    return re(x-1) + 100
print(re(n))