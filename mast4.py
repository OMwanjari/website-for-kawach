n = 3
arr = [1,2,1]
swap = 0
for x in range(n):
    for j in range(x,n-1):
        if arr[j] %2 == 0 and arr[j+1] %2 != 0:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swap +=1

print(swap)
        