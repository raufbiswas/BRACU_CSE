def maxSumSubarray_BruteForceApproach(arr):
  maxSum = float('-inf')
  subarray = []

  for i in range(len(arr)):
    currentSum = 0
    currentSubarray = []
    for j in range(i, len(arr)):
      currentSum += arr[j]
      currentSubarray.append(arr[j])
      if currentSum > maxSum:
        maxSum = currentSum
        subarray = currentSubarray.copy()

  return maxSum, subarray

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
maxSum, subarray = maxSumSubarray_BruteForceApproach(arr)
print("Max Sum:", maxSum)
print("Max Sum Subarray:", subarray)