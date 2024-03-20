inFile = open("input5.txt", "r")
outFile = open("output5.txt", "w")

def quickSort(arr, p, r):
    if p < r:
        temp = partition(arr, p, r)
        quickSort(arr, p, temp -1)
        quickSort(arr, temp + 1, r)
    
def partition(arr, p, r):
    pivot, i =arr[r], p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

#Test Cases
for i in range(4):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n = int(inFile.readline())
    arr = list(map(int, inFile.readline().split()))
    p, r = 0, len(arr)-1
    quickSort(arr, p, r)
    arr = [str(i) for i in arr]
    outFile.write(f"{' '.join(arr)}")

inFile.close()
outFile.close()