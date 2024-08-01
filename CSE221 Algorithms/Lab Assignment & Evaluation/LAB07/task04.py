inFile = open("input4.txt", "r")
outFile = open("output4.txt", "w")

def minimumCoins(n, x, coins):
    ev = [[0] * (x + 1) for i in range(n + 1)]

    for r in range(n + 1):
        for c in range(x + 1):
            if r == 0:
                ev[r][c] = float('inf')
            elif c == 0:
                ev[r][c] = 0
            elif coins[r - 1] > c:
                ev[r][c] = ev[r - 1][c]
            else:
                ev[r][c] = min(ev[r - 1][c], 1 + ev[r][c - coins[r - 1]])
                
    return ev[n][x] if ev[n][x] != float('inf') else -1

for i in range(2):
    if i == 0: outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, x= map(int, inFile.readline().split())
    coins = list(map(int, inFile.readline().split()))
    result = minimumCoins(n, x, coins)
    outFile.write(str(result))

inFile.close()
outFile.close()