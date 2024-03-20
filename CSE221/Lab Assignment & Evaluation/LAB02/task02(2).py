inFile = open("input2.txt", "r")
outFile = open("output2(2).txt", "w")

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


#Test Cases
for i in range(4):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n = int(inFile.readline())
    l1 = list(map(int, inFile.readline().split()))
    m = int(inFile.readline())
    l2 = list(map(int, inFile.readline().split()))
    sortedList = mergeList(n, l1, m, l2)
    finalList = [str(i) for i in sortedList]
    outFile.write(' '.join(finalList))

inFile.close()
outFile.close()