inFile = open("input1.txt", "r")
outFile = open("output1.txt", "w")

def mergeSort(arr):
    l = len(arr)
    if l == 1:
        return arr[0]
    mid = l//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i, j, x = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[x] = left[i]
            i += 1
        elif right[j] < left[i]:
            arr[x] = right[j]
            j += 1
        x += 1
    while i < len(left):
        arr[x] = left[i]
        i, x = i + 1, x + 1
    while j < len(right):
        arr[x] = right[j]
        j, x = j + 1, x + 1

#TestCase 01
outFile.write("Sample Output 01\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
mergeSort(arr)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

#TestCase 02
outFile.write("\n\nSample Output 02\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
mergeSort(arr)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

#TestCase 03
outFile.write("\n\nSample Output 03\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
mergeSort(arr)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

#TestCase 04
outFile.write("\n\nSample Output 04\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
mergeSort(arr)
arr = [str(i) for i in arr]
outFile.write(f"{' '.join(arr)}")

inFile.close()
outFile.close()