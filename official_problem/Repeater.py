txt = input()


for i in range(2,len(txt)*2+2,2):
    
    for j in range(len(txt)*2-i):
        print(' ',end='')
    for k in range(i//2-1,-1,-1):
        print('{} '.format(txt[k]),end='')
        if k == 0 and i!=2:
            for i in range(i//2-1):
                print('{} '.format(txt[i+1]),end='')
        
            
    
    print()
