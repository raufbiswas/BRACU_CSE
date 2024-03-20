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

#Test Cases
for i in range(4):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n = int(inFile.readline())
    arr = list(map(int, inFile.readline().split()))
    result = findMax(arr)
    outFile.write(str(result))

inFile.close()
outFile.close()