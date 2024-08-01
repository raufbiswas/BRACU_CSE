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
    stack = []
    stack.append(start)
    while stack:
        c = stack[len(stack)-1]
        state[c] = 1
        flag = False
        for n in roads[c]:
            if state[n] == 0:
                stack.append(n)
                flag = True
                break
            elif state[n] == 1:
                if n in stack:
                    stack[n] = 2
                    return "YES"
        if not flag:
            stack.pop()
    return "NO"

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
    outFile.write(cycle)