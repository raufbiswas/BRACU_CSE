inFile = open("input1b.txt", "r")
outFile = open("output1b.txt", "w")

def adjacencyList(n, m, graph):
    result = {i:[] for i in range(n+1)}

    # adjacency list
    for i in range(m):
        key, dest, weight = graph[i]
        result[key].append((dest, weight))

    # print output
    for key, val in result.items():
        outFile.write(f"{str(key)} : ")
        for i in range(len(val)):
            outFile.write(f"{str(val[i])}")
            if i != len(val) - 1:
                outFile.write(" ")
        if key != n:
            outFile.write("\n")

# Sample Input
for i in range(3):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    graph = []
    for i in range(m):
        graph.append(list(map(int, inFile.readline().split())))

    adjacencyList(n, m, graph)

inFile.close()
outFile.close()