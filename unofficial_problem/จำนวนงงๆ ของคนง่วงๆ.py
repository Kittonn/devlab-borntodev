n = int(input())
ans = []

for i in range(20):
    for j in range(20):
        for k in range(20):
            ans.append(pow(3, i) * pow(11, j) * pow(19, k))

print(sorted(ans)[n-1])