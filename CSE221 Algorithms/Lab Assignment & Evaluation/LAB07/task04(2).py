inFile = open("input4.txt", "r")
outFile = open("output4.txt", "w")

def minCoins(n, x, coins):
    dp = [float('inf')] * (x + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, x + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[x] if dp[x] <= x else -1

for i in range(2):
    if i == 0: outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, x= map(int, inFile.readline().split())
    coins = list(map(int, inFile.readline().split()))

    result = minCoins(n, x, coins)
    outFile.write(str(result))

inFile.close()
outFile.close()