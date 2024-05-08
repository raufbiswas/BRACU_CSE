inFile = open("input3.txt", "r")
outFile = open("output3.txt", "w")

# Create adjacency list
def adjacencyList(n, m, graph):
    result = {i:[] for i in range(1, n+1)}

    # adjacency list
    for i in range(m):
        u, v = graph[i]
        result[u].append(v)
        result[v].append(u)
    return result

def DFS(roads, start, state):
    path, state[start] = [start], 1
    for neighbour in roads[start]:
        if state[neighbour] == 0:
            path += DFS(roads, neighbour, state)
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
    state = [0] * (n + 1)
    path = DFS(roads, 1, state)
    for i in range(len(path)):
        outFile.write(str(path[i]))
        if i < len(path) - 1:
            outFile.write(" ")

inFile.close()
outFile.close()