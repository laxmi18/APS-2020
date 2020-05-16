def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1],arr[j]
                
arr = [576,2,5,9,43,54]
bubblesort(arr)
print(arr)