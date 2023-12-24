# 3. Find max and min
def array(arr,i=0):
    if i < (len(arr)-1):
        inner(arr,i,j=0) #comparing with every number of the array
        array(arr,i+1)
    return f"{arr}\nMin : {arr[0]} Max : {arr[len(arr)-1]}"

def inner(arr,i,j):
    if j < len(arr)-i-1:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        inner(arr,i,j+1)

arr = [8,5,9,4,2,10,3,1,0,-19,12,6]
print(array(arr))