inFile = open("input3.txt", "r")
outFile = open("output3.txt", "w")  

def countWays(stairs):
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2
    
    dp = [0] * (stairs + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, stairs + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[stairs]


for i in range(4):
    if i == 0: outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    stairs = int(inFile.readline())
    ways = countWays(stairs)
    outFile.write(str(ways))

inFile.close()
outFile.close()
