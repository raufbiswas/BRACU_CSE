inFile = open("input.txt", "r")
outFile = open("output.txt", "w")

def sortfun(u,v,list1,list2):
    i, j, finalList = 0, 0, []
    while i < u and j < v:
        if list1[i] < list2[j]:
            finalList.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            finalList.append(list2[j])
            j += 1
        else:
            finalList.append(list1[i])
            finalList.append(list2[j])
            i , j = i+1, j+1

    finalList += list1[i:] + list2[j:]
    return finalList

for i in range(2):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    u = int(inFile.readline())
    list1 = list(map(int, inFile.readline().split()))
    v = int(inFile.readline())
    list2 = list(map(int, inFile.readline().split()))
    w = int(inFile.readline())
    list3 = list(map(int, inFile.readline().split()))

    mergeFirstTwoList = sortfun(u,v,list1,list2)
    result = sortfun(u+v, w, mergeFirstTwoList, list3)
    finalList = [str(i) for i in result]
    outFile.write(f"{' '.join(finalList)}")

inFile.close()
outFile.close()