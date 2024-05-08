inFile = open("input4.txt", "r")
outFile = open("output4.txt", "w")

# Create adjacency list
def adjacencyList(n, m, graph):
    result = {i:[] for i in range(1, n+1)}

    # adjacency list
    for i in range(m):
        u, v = graph[i]
        result[u].append(v)
    return result

def cycleFinding(roads, start, state, parent):
    state[start] = 1
    for neighbour in roads[start]:
        if state[neighbour] == 0:
            parent[neighbour] = start
            status = cycleFinding(roads, neighbour, state, parent)
            if status:
                return True
        elif state[neighbour] == 1 and parent[start] != neighbour:
            return True
    state[start] = 2
    return False

# Driver Code
# Sample Input
for i in range(5):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    roads = []
    for i in range(m):
        roads.append(list(map(int, inFile.readline().split())))
    roads = adjacencyList(n, m, roads)
    state, parent = [0] * (n + 1), [-1] * (n + 1)
    hasCycle = False
    for i in range(1, n+1):
        if state[i] == 0:
            status = cycleFinding(roads, i, state, parent)
            if status:
                hasCycle = True
                break

    if hasCycle:
        outFile.write("YES")
    else:
        outFile.write("NO")

inFile.close()
outFile.close()