n = input()
num = int(input())
day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thurday', 'friday', 'saturday']

for i in range(len(day)):
    if day[i] == n:
        s = i
s = (s+num)%7
print(day[s])