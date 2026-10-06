def next_permutation(arr):
    i=len(arr)-2
    while i>=0 and arr[i]>=arr[i+1]:
        i-=1
    if i>=0:
        j=len(arr)-1
        while arr[j]<=arr[i]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[i+1:]=reversed(arr[i+1:])
    return arr
arr=[1,3,2]
ob=next_permutation(arr)
print(ob)

