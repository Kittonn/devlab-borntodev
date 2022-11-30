p = ['A','2','3','4','5','6','7','8','9','J','Q','K']
n = list(map(str,input().split()))
s = []
for i in p:
    for j in n:
        if i == j:
            s.append(i)
for i in s:
    print(i,end=' ')