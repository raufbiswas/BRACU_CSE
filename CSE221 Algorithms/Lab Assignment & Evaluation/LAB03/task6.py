inFile = open("input6.txt", "r")
outFile = open("output6.txt", "w")

def smallestNum(arr, p, r, index):
    if p == r:
        if p == index:
            return arr[p]
        return None
    i = partition(arr, p, r)
    if i == index:
        return arr[i]
    elif index < i:
        return smallestNum(arr, p, i - 1, index) 
    return smallestNum(arr, i + 1, r, index)

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
p, r = 0, n - 1
queries = int(inFile.readline())
for i in range(queries):
    index = int(inFile.readline())
    result = smallestNum(arr, p, r, index - 1)
    outFile.write(f'{result}\n')

inFile.close()
outFile.close()