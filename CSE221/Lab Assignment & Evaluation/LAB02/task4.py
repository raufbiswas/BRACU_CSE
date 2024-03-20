inFile = open("input4.txt", "r")
outFile = open("output4.txt", "w")

def maxCompletedTasks(task, peps):
    # Schedule tasks in ascending order of end time to avoid conflicts
    # Selection Sort. Time complexity O(N^2)
    for i in range(n): 
        minEnd = i # Initialize minimum end time index
        for j in range(i+1, n): # Compare with remaining tasks
            if (task[minEnd][1] > task[j][1]) or (task[minEnd][1] == task[j][1]):
                minEnd = j # Update minimum end time index if found
        task[i], task[minEnd] = task[minEnd], task[i] # Swap current task with the task having the earlier end time
    
    # task.sort(key=lambda x: x[1]) or use merge sort to achieve O(nlogn) time complexity.
    
    lpep = [0]*peps # Initialize last completed task time for each person
    lpep[0], count = task[0], 1  # Assign the first task to the first person and update count - Track the maximum completed tasks
    for t in task[1:]: # Iterate through remaining tasks
        temp, flag = [], False  # Store potential time differences for available people and Flag to indicate if an available person was found
        
        # Check if any person is available
        for j in range(peps):
            if lpep[j] == 0:  # If person is available, assign task and update
                lpep[j], count = t, count + 1 # Assign the task and update count
                break # No need to check further, task assigned
            else: # If person is busy, calculate time difference if feasible
                diff = t[0] - lpep[j][1]
                if diff >= 0: # If task start time is after person's last end time
                    temp.append(diff)
                    flag = True
        if flag == True: # If an available person was found, assign based on smallest time difference
            mini = min(temp)
            index = temp.index(mini)
            lpep[index] = t
            count += 1
    outFile.write(str(count))

#Test Cases
for i in range(5):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, m = map(int, inFile.readline().split())
    tasks = []
    for i in range(n):
        tasks.append(list(map(int, inFile.readline().split())))
    maxCompletedTasks(tasks, m)

inFile.close()
outFile.close()