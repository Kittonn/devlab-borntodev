n = input()
n = n.strip("0")
if (n[0] == "-"):
    print("UNDER")
elif (n.isnumeric()):
    if int(n) > 1000000:
        print("OVER")
    else:
        s = 0
        r = len(n)
        while s < len(n):
            print(int(n[s])*pow(10, r-1))
            r -= 1
            s += 1
else:
    print("Invalid")
