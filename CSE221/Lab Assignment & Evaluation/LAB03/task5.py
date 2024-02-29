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

#TestCase 01
outFile.write("Sample Output 01\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
p, r = 0, len(arr)-1
quickSort(arr, p, r)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

#TestCase 02
outFile.write("\n\nSample Output 02\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
p, r = 0, len(arr)-1
quickSort(arr, p, r)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

#TestCase 03
outFile.write("\n\nSample Output 03\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
p, r = 0, len(arr)-1
quickSort(arr, p, r)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

#TestCase 04
outFile.write("\n\nSample Output 04\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
p, r = 0, len(arr)-1
quickSort(arr, p, r)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

inFile.close()
outFile.close()