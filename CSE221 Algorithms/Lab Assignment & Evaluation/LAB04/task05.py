inFile = open("input5.txt", "r")
outFile = open("output5.txt", "w")

# Create adjacency list
def adjacencyList(n, m, graph):
    result = {i:[] for i in range(1, n+1)}

    # adjacency list
    for i in range(m):
        u, v = graph[i]
        result[u].append(v)
        result[v].append(u)
    return result

def shortestPath(roads, start, dest, vertex):
    queue = [(start, [start])]
    state = [0] * (vertex + 1)

    while queue:
        c, path = queue.pop(0)
        state[c] = 1
        if c == dest:
            return path
        for neighbour in roads[c]:
            if state[neighbour] == 0:
                queue.append((neighbour, path + [neighbour]))
                state[neighbour] = 1
    return []

# Driver Code
# Sample Input
for i in range(5):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else:
        outFile.write(f"\n\nSample Output {i+1}\n")

    n, m, d = list(map(int, inFile.readline().split()))
    roads = []
    for j in range(m):
        roads.append(list(map(int, inFile.readline().split())))
    roads = adjacencyList(n, m, roads)
    path = shortestPath(roads, 1, d, n)
    Time = len(path) - 1
    outFile.write(f"Time: {Time}\nShortest Path: ")
    for i in range(len(path)):
        outFile.write(str(path[i]))
        if i < len(path) - 1:
            outFile.write(" ")

inFile.close()
outFile.close()