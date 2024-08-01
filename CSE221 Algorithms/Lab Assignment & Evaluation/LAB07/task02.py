inFile = open("input2.txt", "r")
outFile = open("output2.txt", "w")

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.sizeOfFriendsCircle = [1] * (n + 1)

    def union(self, a, b):
        parentOfA = self.find(a)
        parentOfB = self.find(b)
    
        if parentOfA != parentOfB:
            if self.sizeOfFriendsCircle[parentOfA] < self.sizeOfFriendsCircle[parentOfB]:
                parentOfA, parentOfB = parentOfB, parentOfA
            self.parent[parentOfB] = parentOfA
            self.sizeOfFriendsCircle[parentOfA] += self.sizeOfFriendsCircle[parentOfB]

    def find(self, n):
        if self.parent[n] == n:
            return n
        else:
            self.parent[n] = self.find(self.parent[n])
            return self.parent[n]

def kruskal(roads, n):
    roads.sort(key=lambda x: x[2])
    dsu = DSU(n)
    cost = 0
    for road in roads:
        u, v, w = road
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            cost += w
    return cost

for i in range(2):
    if i == 0: outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = map(int, inFile.readline().split())
    roads = []
    for j in range(m):
        u, v, w = map(int, inFile.readline().split())
        roads.append((u, v, w))
    minCostSet = kruskal(roads, n)
    outFile.write(str(minCostSet))

inFile.close()
outFile.close()
