inFile = open("input1.txt", "r")
outFile = open("output1(1).txt", "w")

def twoSum(n, s, glist):
    for i in range(n): # Iterate through each element in the list
        t = s - glist[i] # Calculate the complement (number needed to reach the target sum)
        pos = False # Flag to indicate if the complement has been found (initially False)
        for j in range(i+1, n): # Inner loop iterates through remaining elements starting from i+1 to avoid duplicates
            if t ==  glist[j]: # Check if the complement is found in the current element
                outFile.write(f"{i+1} {j+1}")
                pos = True # Set the flag to True as the complement has been found
                break # Break out of the inner loop as we found the pair
        if pos == True:
            break # Break out of the outer loop if the complement was found for the current element
    if i == n-1: # Check if the outer loop has iterated through all elements without finding the complement.
       outFile.write("IMPOSSIBLE") # If the outer loop finishes without finding any pair, write "IMPOSSIBLE"

#Test Cases
for i in range(4):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n,s = map(int, inFile.readline().split())
    glist = list(map(int, inFile.readline().split()))
    twoSum(n, s, glist)

inFile.close()
outFile.close()