txt = input()
num = int(input())
if (len(txt) <= num):
    print(txt)
else:
    print(txt[:num]+'...')