inFile = open("input1.txt", "r")
outFile = open("output1(2).txt", "w")

"""
Finds two elements in the given list `glist` that add up to the target sum `s`.

Args:
    n: The number of elements in the list `glist`.
    s: The target sum.
    glist: The list of integers.

Returns:
    None. Instead, writes the indices of the two elements (or "IMPOSSIBLE" if not found) to `outFile`.
"""
def twoSum(n, s, glist):
    l, r = 0, n-1
    while l < r:
        sum = glist[l] + glist[r]
        if sum == s: # Found the pair
            outFile.write(f"{l+1} {r+1}")
            break
        elif sum < s: # Move left pointer if sum is less than target
            l += 1
        elif sum > s: # Move right pointer if sum is greater than target
            r -= 1
        else: # Handle duplicate elements
            l, r = l+1, r-1
    if l == r: # No pair found
        outFile.write("IMPOSSIBLE")

# Testcase 01
outFile.write("Sample Output 1\n")
n,s = map(int, inFile.readline().split())
glist = list(map(int, inFile.readline().split()))
twoSum(n, s, glist)

# Testcase 02
outFile.write("\n\nSample Output 2\n")
n,s = map(int, inFile.readline().split())
glist = list(map(int, inFile.readline().split()))
twoSum(n, s, glist)

# Testcase 03
outFile.write("\n\nSample Output 3\n")
n,s = map(int, inFile.readline().split())
glist = list(map(int, inFile.readline().split()))
twoSum(n, s, glist)

# Testcase 04
outFile.write("\n\nSample Output 4\n")
n,s = map(int, inFile.readline().split())
glist = list(map(int, inFile.readline().split()))
twoSum(n, s, glist)