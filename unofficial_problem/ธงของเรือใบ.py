n = input()
if not(n.isnumeric()):
    print("ERROR please input integer only")
elif (n == '1'):
    print("ERROR please input more than 1")
else:
    n = int(n)
    for i in range(n):
        print("|", end="")
        if i == n-1:
            for j in range(i):
                print("=", end="")
        else:
            for j in range(i):
                print(" ", end="")
        print("\\")
