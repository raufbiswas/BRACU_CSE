inFile = open("input1a.txt", "r")
outFile = open("output1a.txt", "w")

def adjacencyMatrix(n, m, graph):
    result = [[0] * (n+1) for i in range(n+1)]

    # adjacency matrix
    for i in range(m):
        row, col, weight = graph[i]
        result[row][col] = weight

    # print output
    for j in range(n+1):
        result[j] = [str(i) for i in result[j]]
        if j != n:
            outFile.write(f"{' '.join(result[j])}\n")
        else: outFile.write(f"{' '.join(result[j])}")

# Sample Input
for i in range(2):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    graph = []
    for i in range(m):
        graph.append(list(map(int, inFile.readline().split())))

    adjacencyMatrix(n, m, graph)

inFile.close()
outFile.close()