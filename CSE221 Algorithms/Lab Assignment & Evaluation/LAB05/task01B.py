inFile = open("input1.txt", "r")
outFile = open("output1B.txt", "w")

def adjacencyList(n, prerequisites):
    inDegree = [0] * (n + 1)
    result = {i: [] for i in range(1, n + 1)}

    for prerequisite in prerequisites:
        u, v = prerequisite
        result[u].append(v) 
        inDegree[v] += 1

    return [inDegree, result]

def kahnsAlgorithm(n, prerequisites):
    inDegree, prerequisites = adjacencyList(n, prerequisites)
    queue = []

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
    
    sequence, i = [], 0
    while i < len(queue):
        vertex = queue[i]
        i += 1
        sequence.append(vertex)
        for neighbour in prerequisites[vertex]:
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                queue.append(neighbour)
    
    if len(sequence) != n:
        return "IMPOSSIBLE"
    return sequence


for i in range(3):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    prerequisites = []
    for i in range(m):
        prerequisites.append(list(map(int, inFile.readline().split())))
    sequence = kahnsAlgorithm(n, prerequisites)
    if type(sequence) == str:
        outFile.write(sequence)
    else:
        outFile.write(" ".join(str(s) for s in (sequence)))


inFile.close()
outFile.close()