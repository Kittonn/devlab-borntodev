weight = int(input())
height = int(input()) / 100

bmi = weight / (height * height)

if str(bmi)[4] == '0':
  print("BMI: %.1f" % bmi)
else:
  print("BMI: %.2f" % bmi)
