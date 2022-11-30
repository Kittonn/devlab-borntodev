n = int(input())
if n % 3 == 0 and n % 2 == 0:
    print('FizzBuzz')
elif n% 3 == 0:
    print('Fizz')
else:
    print('Buzz')