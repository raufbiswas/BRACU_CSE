inFile = open("input4.txt", "r")
outFile = open("output4.txt", "w")

def maximumSum(arr):
    l = len(arr)
    if l == 1:
        return -99999999
    elif l == 2:
        return arr[0] + arr[1]**2
       
    mid = l//2
    left, right = arr[:mid], arr[mid:]

    leftSum = maximumSum(left)
    rightSum = maximumSum(right)

    leftMax = left[0]
    for i in range(1, len(left)):
        if left[i] > leftMax:
            leftMax = left[i]
    
    rightMax = right[0]**2
    for j in range(1, len(right)):
        if right[j]**2 > rightMax:
            rightMax = right[j]**2

    return max(leftSum, rightSum, leftMax + rightMax)


#TestCase 01
outFile.write("Sample Output 01\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = maximumSum(arr)
outFile.write(str(result))

#TestCase 02
outFile.write("\n\nSample Output 02\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = maximumSum(arr)
outFile.write(str(result))

#TestCase 03
outFile.write("\n\nSample Output 03\n")
n = int(inFile.readline())
arr = list(map(int, inFile.readline().split()))
result = maximumSum(arr)
outFile.write(str(result))

inFile.close()
outFile.close()