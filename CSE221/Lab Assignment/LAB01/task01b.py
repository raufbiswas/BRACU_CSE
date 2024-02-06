#Task01b
inFile = open("input1b.txt", 'r')
outFile = open("output1b.txt", "w")

N = int(inFile.readline())

for i in range(N):
    # split the string based on space(' ') and then I choose the last 3 elements because 
    # these three elements are the two operands and the operator.
    operand2, operator, operand1 = inFile.readline().split()[-1:-4:-1]

    # add, subtract, multiply or divide based on the operator
    if operator == '+':
        result = int(operand1) + int(operand2)
    elif operator == '-':
        result = int(operand1) - int(operand2)
    elif operator == '*':
        result = int(operand1) * int(operand2)
    elif operator == '/':
        result = round(int(operand1)/int(operand2), 1)

    if i < N - 1:
        outFile.write(f"The result of {operand1} {operator} {operand2} is {result}\n")
    else:
        outFile.write(f"The result of {operand1} {operator} {operand2} is {result}")

inFile.close()
outFile.close()