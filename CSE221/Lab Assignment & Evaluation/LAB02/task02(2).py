inFile = open("input2.txt", "r")
outFile = open("output2(2).txt", "w")

"""
Merges two sorted lists `l1` and `l2` into a single sorted list.

Args:
    n: Length of the first list `l1`.
    l1: The first sorted list.
    m: Length of the second list `l2`.
    l2: The second sorted list.

Returns:
    A new list containing the elements of `l1` and `l2` in sorted order.
"""
def mergeList(n, l1, m, l2):
    i, j, sortedList = 0, 0, []
    while i < n and j < m: # Loop while both lists have elements
        if l1[i] > l2[j]: # If element in l1 is greater
            sortedList.append(l2[j])
            j += 1
        elif l1[i] < l2[j]: # If element in l1 is smaller
            sortedList.append(l1[i])
            i += 1
        else: # If elements are equal
            sortedList.append(l1[i])
            sortedList.append(l2[j])
            i, j = i+1, j+1

    sortedList += l1[i:] + l2[j:] # Copy remaining elements from l1 and l2 (if any)
    return sortedList


# Testcase 01
outFile.write("Sample Output 1\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = mergeList(n, l1, m, l2)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))

# Testcase 02
outFile.write("\n\nSample Output 2\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = mergeList(n, l1, m, l2)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))

# Testcase 03
outFile.write("\n\nSample Output 3\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = mergeList(n, l1, m, l2)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))

# Testcase 04
outFile.write("\n\nSample Output 4\n")
n = int(inFile.readline())
l1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
l2 = list(map(int, inFile.readline().split()))
sortedList = mergeList(n, l1, m, l2)
finalList = [str(i) for i in sortedList]
outFile.write(' '.join(finalList))