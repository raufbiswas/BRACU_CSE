inFile = open("input2.txt", "r")
outFile = open("output2.txt", "w")

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

def meetTimeAndNode(sourceDistances, targetDistances, n):
    minTime = float('inf')
    meetNode = -1
    for node in range(1, n + 1):
        if node in sourceDistances and node in targetDistances:
            time = max(sourceDistances[node], targetDistances[node])
            if time < minTime:
                minTime = time
                meetNode = node
    return (minTime, meetNode)

for i in range(3):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else:
        outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = map(int, inFile.readline().split())
    paths = []
    for i in range(m):
        paths.append(list(map(int, inFile.readline().split())))
    sourceNode, targetNode = map(int, inFile.readline().split())
    paths = adjacencyList(n, paths)
    sourceDistances = dijkstraAlgorithm(paths, sourceNode)
    targetDistances = dijkstraAlgorithm(paths, targetNode)
    minTime, meetNode = meetTimeAndNode(sourceDistances, targetDistances, n)
    if minTime == float('inf'):
        outFile.write("Impossible")
    else:
        outFile.write(f"Time {minTime}\nNode {meetNode}")

inFile.close()
outFile.close()