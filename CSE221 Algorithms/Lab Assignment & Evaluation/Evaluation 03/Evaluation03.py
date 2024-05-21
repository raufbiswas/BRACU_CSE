inFile = open("input.txt", "r")
outFile = open("output.txt", "w")

def adjacencyList(n, m, graph):
    result = {i: [] for i in range(1, n+1)}

    for i in range(m):
        u, v = graph[i]
        result[u].append(v)
    return result

def DFS(roads, vertex, visited, stack):
    visited[vertex] = 1
    for neighbour in roads[vertex]:
        if visited[neighbour] == 0:
            DFS(roads, neighbour, visited, stack)
    stack.append(vertex)

def kosarajusAlgorithm(n, roads):
    roads = adjacencyList(n, len(roads), roads)
    stack = []
    visited = [0] * (n + 1)

    for vertex in range(1, n + 1):
        if visited[vertex] == 0:
            DFS(roads, vertex, visited, stack)

    reversedRoads = {i: [] for i in range(1, n + 1)}
    for u in roads:
        for v in roads[u]:
            reversedRoads[v].append(u)

    visited = [0] * (n + 1)
    scComponents = []

    while stack:
        vertex = stack.pop()
        if visited[vertex] == 0:
            scComponent = []
            DFS(reversedRoads, vertex, visited, scComponent)
            scComponents.append(scComponent)

    return scComponents

def hasCycle(n, roads, node):
    scComponents = kosarajusAlgorithm(n, roads)
    for scComponent in scComponents:
        if node in scComponent and len(scComponent) > 1:
            return True
    return False

outFile.write("Sample Output\n")
n, m = list(map(int, inFile.readline().split()))
roads = []
for i in range(m):
    roads.append(list(map(int, inFile.readline().split())))

for i in range(1, n + 1):
    if hasCycle(n, roads, i):
        outFile.write(f"Node {i} Yes")
    else:
        outFile.write(f"Node {i} No")
    if i < n:
        outFile.write("\n")

inFile.close()
outFile.close()