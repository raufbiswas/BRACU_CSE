inFile = open("input1.txt", "r")
outFile = open("output1.txt", "w")

def adjacencyList(n, paths):
    result = {i: [] for i in range(1, n + 1)}

    for path in paths:
        u, v, w = path
        result[u].append((v, w))

    return result

import heapq
def dijkstraAlgorithm(paths, sourceNode):
    distances = {n: float('inf') for n in paths}
    distances[sourceNode] = 0
    queue = [(0, sourceNode)]

    while queue:
        currentDistance, currentNode = heapq.heappop(queue)
        if currentDistance > distances[currentNode]:
            continue
        for neighbour, w in paths[currentNode]:
            if currentDistance + w < distances[neighbour]:
                distances[neighbour] = currentDistance + w
                heapq.heappush(queue, (currentDistance + w, neighbour))

    return distances



for i in range(2):
    if i == 0: outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    paths = []
    for i in range(m):
        paths.append(list(map(int, inFile.readline().split())))
    paths = adjacencyList(n, paths)
    sourceNode = int(inFile.readline())
    distances = dijkstraAlgorithm(paths, sourceNode)
    for node in range(1, n+1):
        if distances[node] == float('inf'):
            outFile.write("-1")
        else:
            outFile.write(str(distances[node]))
        if node != n: outFile.write(" ")

inFile.close()
outFile.close()