num = [1,2,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
n = int(input())
t = -1
if n not in num:
    print(-1)
else:   
    for i in num:
        t += 1
        if i == n:
            break
    print(t)