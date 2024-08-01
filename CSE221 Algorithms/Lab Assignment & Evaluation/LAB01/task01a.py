#Task01a
inFile = open("input1a.txt", 'r')
outFile = open("output1a.txt", "w")

N = int(inFile.readline())

for i in range(N):
    num = int(inFile.readline()) # read the num

    # divide the num by 2 and check if the number is even or odd
    if num%2 == 0: evod = "Even" 
    else: evod = "Odd"

    if i < N - 1:
        outFile.write(f"{num} is an {evod} number.\n")
    else:
        outFile.write(f"{num} is an {evod} number.")

inFile.close()
outFile.close()