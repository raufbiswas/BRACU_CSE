inFile = open("input3.txt", "r")
outFile = open("output3.txt", "w")

def dividingArr(arr):
    l = len(arr)
    if l <= 1:
        return 0
        
    mid = l//2
    left = arr[:mid]
    right = arr[mid:]
    
    return dividingArr(left) + dividingArr(right) + sortAndCount(arr, left, right)

def sortAndCount(arr, left, right):
    i, j, x, count = 0, 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[x] = left[i]
            i += 1
        else:
            arr[x] = right[j]
            count += len(left) - i
            j += 1
        x += 1

    while i < len(left):
        arr[x] = left[i]
        i, x = i + 1, x + 1
    while j < len(right):
        arr[x] = right[j]
        j, x = j + 1, x + 1

    return count

#TestCase 01
outFile.write("Sample Output 01\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = dividingArr(arr)
outFile.write(str(result))

#TestCase 02
outFile.write("\n\nSample Output 02\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = dividingArr(arr)
outFile.write(str(result))

#TestCase 03
outFile.write("\n\nSample Output 03\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = dividingArr(arr)
outFile.write(str(result))

inFile.close()
outFile.close()