def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        L=a[:mid]
        R=a[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                a[k]=L[i]
            else:
                a[k]=R[j]
                j+=1
        while i<len(L):
            a[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            a[k]=R[j]
            j+=1
            k+=1

a=[58,2,5,12,322,67]
mergeSort(a)
print(a)                    