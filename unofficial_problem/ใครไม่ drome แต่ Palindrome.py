n = input()
num = len(n)
num2 = num // 2
x = ''.join(reversed(n[:num2]))
if (n[num2:] == x):
    print('{} is a palindrome.'.format(n))
else:
    print('{} is not a palindrome.'.format(n))