inFile = open("input.txt", "r")
outFile = open("output.txt", "w")
def mergeList(arr):
    l = len(arr)
    if l > 1:
        mid = l//2
        left = arr[:mid]
        right = arr[mid:]
        mergeList(left)
        mergeList(right)
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

n = int(inFile.readline())
list1 = list(map(int, inFile.readline().split()))
m = int(inFile.readline())
list2 = list(map(int, inFile.readline().split()))
k = int(inFile.readline())
arr = list1+list2
mergeList(arr)
outFile.write(str(arr[k-1]))
inFile.close()
outFile.close()