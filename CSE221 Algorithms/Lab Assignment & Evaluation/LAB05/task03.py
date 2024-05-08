inFile = open("input3.txt", "r")
outFile = open("output3.txt", "w")

def adjacencyList(n, prerequisites):
    result = {i: [] for i in range(1, n + 1)}

    for prerequisite in prerequisites:
        u, v = prerequisite
        result[u].append(v)

    return result

def DFS(prerequisites, vertex, visited, stack):
    visited[vertex] = 1
    for neighbour in prerequisites[vertex]:
        if visited[neighbour] == 0:
            DFS(prerequisites, neighbour, visited, stack)
    stack.append(vertex)

def kosarajusAlgorithm(n, prerequisites):
    prerequisites = adjacencyList(n, prerequisites)
    stack = []
    visited = [0] * (n + 1)

    for vertex in range(1, n + 1):
        if visited[vertex] == 0:
            DFS(prerequisites, vertex, visited, stack)

    reversed = {i: [] for i in range(1, n + 1)}
    for u in prerequisites:
        for v in prerequisites[u]:
            reversed[v].append(u)

    visited = [0] * (n + 1)
    scComponents = []

    while stack:
        vertex = stack.pop()
        if visited[vertex] == 0:
            scComponent = []
            DFS(reversed, vertex, visited, scComponent)
            scComponents.append(scComponent)

    return scComponents


for i in range(3):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else:
        outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    prerequisites = []
    for i in range(m):
        prerequisites.append(list(map(int, inFile.readline().split())))

    scComponents = kosarajusAlgorithm(n, prerequisites)
    scComponents.sort()

    # Soring is unnecessary because order does not matter.
    for scComponent in scComponents:
        scComponent.sort()
        outFile.write(" ".join(map(str, scComponent)))
        if scComponents.index(scComponent) < len(scComponents) - 1:
            outFile.write("\n")

inFile.close()
outFile.close()