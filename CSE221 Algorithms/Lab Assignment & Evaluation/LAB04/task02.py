inFile = open("input2.txt", "r")
outFile = open("output2.txt", "w")

# Create adjacency list
def adjacencyList(n, m, graph):
    result = {i:[] for i in range(1, n+1)}

    # adjacency list
    for i in range(m):
        u, v = graph[i]
        result[u].append(v)
        result[v].append(u)
    return result

def BFS(roads, start, vertex):
    queue, path = [start], []
    state = [0]*(vertex + 1)
    state[start] = 1
    while queue:
        c = queue.pop(0)
        path.append(c)
        for neighbour in roads[c]:
            if state[neighbour] == 0:
                queue.append(neighbour)
                state[neighbour] = 1
    return path

# Driver Code
# Sample Input
for i in range(4):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    roads = []
    for i in range(m):
        roads.append(list(map(int, inFile.readline().split())))
    roads = adjacencyList(n, m, roads)
    path = BFS(roads, 1, n)
    for i in range(len(path)):
        outFile.write(str(path[i]))
        if i < len(path) - 1:
            outFile.write(" ")

inFile.close()
outFile.close()