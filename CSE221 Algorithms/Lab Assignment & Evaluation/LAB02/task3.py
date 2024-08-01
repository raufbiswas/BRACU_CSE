inFile = open("input3.txt", "r")
outFile = open("output3.txt", "w")

def taskManagement(n, task):
    # Schedule tasks in ascending order of end time to avoid conflicts
    # Selection Sort. Time complexity O(N^2)
    for i in range(n):
        minEnd = i # Initialize minimum end time index
        for j in range(i+1, n): # Compare with remaining tasks
            if (task[minEnd][1] > task[j][1]) or (task[minEnd][1] == task[j][1]):
                minEnd = j # Update minimum end time index if found
        task[i], task[minEnd] = task[minEnd], task[i] # Swap current task with the task having the earlier end time
    # task.sort(key=lambda x: x[1])
        
    # Select non-overlapping tasks and update end time for next iteration    
    result, endT = [], 0
    for t in task:
        if t[0] >= endT: # Check if task start time is after previous task end time
            result.append(t)
            endT = t[1] # Update end time for next task scheduling

    outFile.write(str(len(result)))
    for t in result:
        outFile.write("\n")
        outFile.write(f"{t[0]} {t[1]}")

#Test Cases
for i in range(3):
    if i == 0: outFile.write(f"Sample Output 1\n")
    else: outFile.write(f"\n\nSample Output {i+1}\n")
    n, tasks = int(inFile.readline()), []
    for i in range(n):
        tasks.append(list(map(int, inFile.readline().split())))
    taskManagement(n, tasks)

inFile.close()
outFile.close()