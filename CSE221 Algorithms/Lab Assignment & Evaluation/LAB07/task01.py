inFile = open("input1.txt", "r")
outFile = open("output1.txt", "w")

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
            self.sizeOfFriendsCircle[parentOfA] += self.sizeOfFriendsCircle[parentOfB
                                                                            ]
        return self.sizeOfFriendsCircle[self.find(a)]
    
    def find(self, n):
        if self.parent[n] == n:
            return n
        else:
            self.parent[n] = self.find(self.parent[n])
            return self.parent[n]

for i in range(2):
    if i == 0: outFile.write("Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, k = map(int, inFile.readline().split())
    dsu = DSU(n)
    for j in range(k):
        a, b = map(int, inFile.readline().split())
        outFile.write(str(dsu.union(a, b)))
        if j < k - 1:
            outFile.write("\n") 

inFile.close()
outFile.close()