def main():
    n = int(input())
    print(fac(n))

def fac(n):
    if n <= 1:
        return 1
    else:
        return n* fac (n-1)
main()