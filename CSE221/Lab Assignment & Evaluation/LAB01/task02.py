inFile = open('input2.txt', 'r')
outFile = open('output2.txt', 'w')

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]: # compare two number and swap if needed
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # swap position if the value of index j is greater than the value of index j + 1
                swapped = True # flag is true means elements swapped there positions.

        # if flag is False it means no elements changed there position,
        # the array is sorted already.
        if swapped is False:
            break
        # as the array is sorted no need to run the loop anymore.
        # break the loop so that it doesn't run n*n = n^2 times.
        # it will achieve θ(n) time complexity for the best-case scenario.

#Test Cases
for i in range(2):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n = int(inFile.readline())
    arr = list(map(int, inFile.readline().split()))
    bubbleSort(arr)
    outFile.write(' '.join(map(str, arr)))

inFile.close()
outFile.close()


# Explanation
# I take a flag to check if any swaps are made or not. Suppose, the elements of the array are already in sorted order.
# But if the elements are not in sorted order, elements will swap their position inside the second loop and the flag will become True.
# Then again when the first loop runs flag will become False again.
# If no swaps are made in any pass it means the array is sorted and at this time as the flag is False it will break the loop.
# As, the loops will not run anymore, it will achieve the θ(n) for the best-case scenario.