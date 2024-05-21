inFile = open("input3.txt", "r")
outFile = open("output3.txt", "w")

def adjacencyList(n, paths):
    result = {i: [] for i in range(1, n + 1)}

    for path in paths:
        u, v, w = path
        result[u].append((v, w))

    return result

import heapq
def dijkstraAlgorithm(paths, sourceNode):
    distances = {n: float('inf') for n in range(1, len(paths) + 1)}
    distances[sourceNode] = 0
    queue = [(0, sourceNode)]

    while queue:
        currentDistance, currentNode = heapq.heappop(queue)
        if currentDistance > distances[currentNode]:
            continue
        for neighbour, w in paths[currentNode]:
            danger = max(distances[currentNode], w)
            if danger < distances[neighbour]:
                distances[neighbour] = danger
                heapq.heappush(queue, (distances[neighbour], neighbour))

    return distances

for i in range(2):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else:
        outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = map(int, inFile.readline().split())
    paths = []
    for i in range(m):
        paths.append(list(map(int, inFile.readline().split())))
    paths = adjacencyList(n, paths)
    sourceNode = 1
    distances = dijkstraAlgorithm(paths, sourceNode)

    if distances[n] == float('inf'):
        outFile.write("Impossible")
    else:
        outFile.write(str(distances[n]))

inFile.close()
outFile.close()