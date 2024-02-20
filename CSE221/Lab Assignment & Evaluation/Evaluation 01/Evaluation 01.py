inFile = open("input1.txt", "r")
outFile = open("output1.txt", "w")

def sortfun(u,v,w,lst1,lst2,lst3):
    i, j, temp = 0, 0, []
    while i < u and j < v:
        if lst1[i] < lst2[j]:
            temp.append(lst1[i])
            i += 1
        elif lst2[j] < lst1[i]:
            temp.append(lst2[j])
            j += 1
        else:
            temp.append(lst1[i])
            temp.append(lst2[j])
            i , j = i+1, j+1

    temp += lst1[i:] + lst2[j:]
    flist, k, j = [], 0, 0

    while k < len(temp) and j < w:
        if temp[k] < lst3[j]:
            flist.append(temp[k])
            k += 1
        elif lst3[j] < temp[k]:
            flist.append(lst3[j])
            j += 1
        else:
            flist.append(temp[k])
            flist.append(lst3[j])
            k , j = k+1, j+1

    flist += temp[k:] + lst3[j:]
    return flist

# 01
u = int(inFile.readline())
lst1 = list(map(int, inFile.readline().split()))
v = int(inFile.readline())
lst2 = list(map(int, inFile.readline().split()))
w = int(inFile.readline())
lst3 = list(map(int, inFile.readline().split()))

result = sortfun(u,v,w,lst1,lst2,lst3)
temp = [str(i) for i in result]
outFile.write(f"{' '.join(temp)}")

# 02
outFile.write("\n")
u = int(inFile.readline())
lst1 = list(map(int, inFile.readline().split()))
v = int(inFile.readline())
lst2 = list(map(int, inFile.readline().split()))
w = int(inFile.readline())
lst3 = list(map(int, inFile.readline().split()))

result = sortfun(u,v,w,lst1,lst2,lst3)
temp = [str(i) for i in result]
outFile.write(f"{' '.join(temp)}")

inFile.close()
outFile.close()