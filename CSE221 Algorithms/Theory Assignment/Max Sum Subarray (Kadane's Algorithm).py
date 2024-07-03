def maxSumSubarray_KadanesAlgorithm(arr):
    maxSum = currentSum = arr[0]
    start = end = s = 0
    
    for i in range(1, len(arr)):
        if arr[i] > currentSum + arr[i]:
            currentSum = arr[i]
            s = i
        else:
            currentSum += arr[i]
        
        if currentSum > maxSum:
            maxSum = currentSum
            start = s
            end = i

    return maxSum, arr[start:end + 1]  # Return sum and subarray

# Example usage
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
maxSum, subarray = maxSumSubarray_KadanesAlgorithm(arr)
print("Max Sum:", maxSum)
print("Max Sum Subarray:", subarray)