inFile = open("input4.txt", "r")
outFile = open("output4.txt", "w")

def railwayManagement(trainSchedule):
    for i in range(len(trainSchedule) - 1):
        swapped = False

        for j in range(len(trainSchedule) - i - 1):
            # compare the names of the trains and sort the trains in the lexicographical order based on the name of the trains.
            if trainSchedule[j][0] > trainSchedule[j + 1][0]:
                trainSchedule[j], trainSchedule[j + 1] = trainSchedule[j + 1], trainSchedule[j]
                swapped = True
            elif trainSchedule[j][0] == trainSchedule[j + 1][0]: # if the name of two or more trains are same
                # compare the departure times of the trains and sorting the trains in the lexicographical order based on the departure times of the trains.
                if trainSchedule[j][2] != trainSchedule[j+1][2]: 
                    time1, time2 = trainSchedule[j][2].split(':'), trainSchedule[j+1][2].split(':') # split the time in hours and minutes
                    if time1[0] == time2[0]:  # if the departure hours of the trains are same then comparing the departure minutes are enough for sorting
                        if int(time1[1]) < int(time2[1]):
                            trainSchedule[j], trainSchedule[j + 1] = trainSchedule[j + 1], trainSchedule[j]
                    else:  # if the departure hours of the trains are not same then comparing the departure hours are enough for sorting
                        if int(time1[0]) < int(time2[0]):
                            trainSchedule[j], trainSchedule[j + 1] = trainSchedule[j + 1], trainSchedule[j]
                    swapped = True
                # if the departure times are also same then automatically the train with the latest departure time will get prioritized.

        if swapped is False: break # if the flag is false it means the trains are already grouped in sorted order.

n = int(inFile.readline())
trainSchedule = []

for i in range(n):
    trainDetails = inFile.readline().split() # spliting the string and store the train name, location and departure time
    trainSchedule.append([trainDetails[0], trainDetails[4], trainDetails[6]]) # pass the information as arguments
railwayManagement(trainSchedule)

for i in range(n):
    if i < n - 1:
        outFile.write(f"{trainSchedule[i][0]} will departure for {trainSchedule[i][1]} at {trainSchedule[i][2]}\n")
    else:
        outFile.write(f"{trainSchedule[i][0]} will departure for {trainSchedule[i][1]} at {trainSchedule[i][2]}")

inFile.close()
outFile.close()