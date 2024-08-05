n = 4 #input
pro = 2
res = 2

for x in range(3,n):
    if pro % n == 1:
        print(res)
        break
    elif x == n-1:
        print(1)
    pro*=x
    res+=1
    
