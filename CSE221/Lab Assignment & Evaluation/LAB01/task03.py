inFile = open("input3.txt", "r")
outFile = open("output3.txt", "w")

def rankStudents(arrID, arrMarks): # selection sort technique
    n = len(arrMarks)
    
    for i in range(n):
        maxIndex = i # let's assume that i is the maximum value index
        for j in range(i + 1, n): # for comparing i with it's next elements and finding the highest value index.
            # comparing marks and identifying the maximum value in each iteration. if marks are same then identifying the lowest id.
            if arrMarks[j] > arrMarks[maxIndex] or (arrMarks[j] == arrMarks[maxIndex] and arrID[j] < arrID[maxIndex]):
                maxIndex = j 
                
        # positioning the minimum/maximum element in its rightful place with a solitary swap.
        arrID[i], arrID[maxIndex] = arrID[maxIndex], arrID[i] # swaping marks
        arrMarks[i], arrMarks[maxIndex] = arrMarks[maxIndex], arrMarks[i] # swapping ID's

#Test Cases
for i in range(2):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n = int(inFile.readline())
    arrID = list(map(int, inFile.readline().split()))
    arrMarks = list(map(int, inFile.readline().split()))
    rankStudents(arrID, arrMarks)
    for i in range(n):
        if i < n - 1:
            outFile.write(f"ID: {arrID[i]} Mark: {arrMarks[i]}\n")
        else:
            outFile.write(f"ID: {arrID[i]} Mark: {arrMarks[i]}")

inFile.close()
outFile.close()

# Selection sort minimizes the number of swaps by only performing swaps when identifying the minimum/maximum value in each iteration.
# It divides the array into a sorted portion and an unsorted portion,
# consistently positioning the minimum/maximum element in its rightful place with a solitary swap.
# In selection sort, if my arr length is N,
# this sorting technique sorts the array by performing a maximum of N - 1 swaps.
# to arrange the elements in ascending or descending order.