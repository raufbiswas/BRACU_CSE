inFile = open("input2.txt", "r")
outFile = open("output2.txt", "w")

def findMax(arr):
    l = len(arr)
    if l == 1:
        return arr[0]
    
    mid = l//2
    left = arr[:mid]
    right = arr[mid:]
    maxLeft = findMax(left)
    maxRight = findMax(right)
    
    return maxLeft if maxLeft > maxRight else maxRight

#TestCase 01
outFile.write("Sample Output 01\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = findMax(arr)
outFile.write(str(result))

#TestCase 02
outFile.write("\n\nSample Output 02\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = findMax(arr)
outFile.write(str(result))

#TestCase 03
outFile.write("\n\nSample Output 03\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = findMax(arr)
outFile.write(str(result))

#TestCase 04
outFile.write("\n\nSample Output 04\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = findMax(arr)
outFile.write(str(result))

inFile.close()
outFile.close()