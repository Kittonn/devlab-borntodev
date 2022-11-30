p = int(input())
print('1000 * {}'.format(p //1000))
print('500 * {}'.format((p % 1000) // 500))
print('100 * {}'.format(((p % 1000)%500) // 100))