#task2a
inFile = open("input2.txt", "r")
outFile = open("output2(1).txt", "w")

"""
This function sorts the given list `arr` using the merge sort algorithm.

Args:
    arr: The list to be sorted.

Returns:
    None. Modifies the input list `arr` in-place to contain the sorted elements.
"""
def mergeList(arr):
    l = len(arr)
    if l > 1:
        # Divide the list into two halves (recursively):
        mid = l//2
        left = arr[:mid]
        right = arr[mid:]
        mergeList(left) # Sort the left half
        mergeList(right) # Sort the right half

        # Merge the sorted halves:
        i, j, x = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]: # Compare elements from left and right halves
                arr[x] = left[i]
                i += 1
            elif right[j] < left[i]:
                arr[x] = right[j]
                j += 1
            x += 1

        while i < len(left): # Copy remaining elements from the left half, if any
            arr[x] = left[i]
            i, x = i + 1, x + 1
        while j < len(right): # Copy remaining elements from the right half, if any
            arr[x] = right[j]
            j, x = j + 1, x + 1
    # else:
          # Base case: If the list has only one element, it's already sorted. 
            
# Testcase 01
outFile.write("Sample Output 1\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = l1+l2
mergeList(sortedList)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))

# Testcase 02
outFile.write("\n\nSample Output 2\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = l1+l2
mergeList(sortedList)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))

# Testcase 03
outFile.write("\n\nSample Output 3\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = l1+l2
mergeList(sortedList)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))

# Testcase 04
outFile.write("\n\nSample Output 4\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = l1+l2
mergeList(sortedList)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))