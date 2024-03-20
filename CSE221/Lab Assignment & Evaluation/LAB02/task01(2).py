inFile = open("input1.txt", "r")
outFile = open("output1(2).txt", "w")

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

#Test Cases
for i in range(4):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n,s = map(int, inFile.readline().split())
    glist = list(map(int, inFile.readline().split()))
    twoSum(n, s, glist)

inFile.close()
outFile.close()