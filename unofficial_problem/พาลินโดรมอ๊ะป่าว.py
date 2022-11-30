n = input().lower()
if n == "".join(list(n)[::-1]):
  print("Yes")
else:
  print("No")