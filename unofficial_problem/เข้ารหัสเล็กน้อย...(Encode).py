txt = list(input())
ans = [chr(ord(i)+4) for i in txt]
t = ''.join(ans)
print(t)