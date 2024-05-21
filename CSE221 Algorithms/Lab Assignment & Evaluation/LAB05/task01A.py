inFile = open("input1.txt", "r")
outFile = open("output1A.txt", "w")

def adjacencyList(n, prerequisites):
    result = {i: [] for i in range(1, n + 1)}

    for prerequisite in prerequisites:
        u, v = prerequisite
        result[u].append(v)

    return result

def DFS(prerequisites, vertex, visited, stack, cycle):
    visited[vertex] = 1
    cycle.append(vertex)

    for neighbour in prerequisites[vertex]:
        if visited[neighbour] == 0:
            if DFS(prerequisites, neighbour, visited, stack, cycle):
                return True
        elif visited[neighbour] == 1:
            if neighbour in cycle:
                return True

    cycle.pop()
    visited[vertex] = 2
    stack.append(vertex)
    return False

def courseSequence(n, prerequisites):
    prerequisites = adjacencyList(n, prerequisites)
    visited = [0] * (n + 1)
    stack, cycle = [], []

    for vertex in range(1, n + 1):
        if visited[vertex] == 0:
            if DFS(prerequisites, vertex, visited, stack, cycle):
                return "IMPOSSIBLE"

    stack.reverse()
    return stack


for i in range(3):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    prerequisites = []
    for i in range(m):
        prerequisites.append(list(map(int, inFile.readline().split())))
    sequence = courseSequence(n, prerequisites)
    if type(sequence) == str:
        outFile.write(sequence)
    else:
        outFile.write(" ".join(str(s) for s in (sequence)))


inFile.close()
outFile.close()