def rotate(arr,k):
    n=len(arr)
    k= k % n
    def reversearr(start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    reversearr(0,n-1)
    reversearr(0,k-1)
    reversearr(k,n-1)
    return arr
arr = [1,2,3,4,5,6,7]
k = 3
print("Rotated Array:", rotate(arr, k))


