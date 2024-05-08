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

def cycleFinding(roads, start, state):
    state[start] = 1
    for i in roads[start]:
        if state[i] == 1 or cycleFinding(roads, i, state) == 1:
            return 1
    state[start] = 0
    return 0

# Driver Code
for i in range(5):
    if i == 0:
        outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = list(map(int, inFile.readline().split()))
    roads = []
    for i in range(m):
        roads.append(list(map(int, inFile.readline().split())))
    roads = adjacencyList(n, m, roads)
    cycle = cycleFinding(roads, 1, [0] * (n + 1))
    if cycle == 1:
        outFile.write("YES")
    else:
        outFile.write("NO")