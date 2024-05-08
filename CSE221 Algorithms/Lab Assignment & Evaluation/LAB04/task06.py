inFile = open("input6.txt", "r")
outFile = open("output6.txt", "w")

def maxDiamonds(jungleMap):
    count, rows, cols= 0, len(jungleMap), len(jungleMap[0])
    state = [[0] * cols for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if jungleMap[row][col] == '.':
                count = max(count, countAndTrack(jungleMap, state, row, col))
    
    return count

def countAndTrack(jungleMap, state, row, col):
    if (row < 0 or row >= len(jungleMap)) or (col < 0 or col >= len(jungleMap[0])) or jungleMap[row][col] == '#' or state[row][col] == 1:
        return 0
    
    state[row][col], diamonds = 1, 0
    if jungleMap[row][col] == 'D': diamonds = 1
    diamonds += countAndTrack(jungleMap, state, row + 1, col) + countAndTrack(jungleMap, state, row - 1, col)
    diamonds += countAndTrack(jungleMap, state, row, col + 1) + countAndTrack(jungleMap, state, row, col - 1)
    
    return diamonds

# Sample Input
for i in range(7):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else:
        outFile.write(f"\n\nSample Output {i+1}\n")
    r, h = map(int, inFile.readline().split())
    jungleMap = []
    for i in range(r):
        jungleMap += [inFile.readline().strip()]
    count = maxDiamonds(jungleMap)
    outFile.write(str(count))

inFile.close()
outFile.close()