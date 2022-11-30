num = int(input())
count = [0, 0, 0, 0, 0]
mod = [1000, 500, 100, 50, 20]

for i in range(5):
  count[i] = num // mod[i]
  num %= mod[i]
for i in range(5):
  print(f"{count[i]} {mod[i]} THB")