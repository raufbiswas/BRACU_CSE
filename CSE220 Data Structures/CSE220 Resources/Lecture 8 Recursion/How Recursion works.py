# >>> Recursion <<<
# 1. A method call itself.
# 2. Exit condition to exit from infinite loop.

# Example 01
# Write a function which recursively print numbers from 1 to n.
def recursiveMethod(parameter):
    if parameter < 1:
        print("Exit condition Satisfied. Exited.")
    else:
        recursiveMethod(parameter-1)
        print(parameter)

print(">> Output of Example 01 <<")
recursiveMethod(4)

# Please visit this link (http://tinyurl.com/howRecursionworks)
# Stack
# push --> recursiveMethod(4) > recursiveMethod(3) > recursiveMethod(2) > recursiveMethod(1)
# as 0 is less than 1 no need to store recursiveMethod(0) in stack.
# start executing the output.
# print "Exit condition Satisfied. Exited."
# pop
# recursiveMethod(4) > recursiveMethod(3) > recursiveMethod(2)
# recursiveMethod(4) > recursiveMethod(3)
# recursiveMethod(4)
# All function popped out.
# Final output: Exit condition Satisfied. Exited. 1 2 3 4

#Example 02
def firstMethod():
    print("First Method")
    secondMethod()

def secondMethod():
    print("Second Method")
    thirdMethod()
    
def thirdMethod():
    print("Third Method")
    fourthMethod()

def fourthMethod():
    print("Fourth or Last Method")

print(">> Output of Example 02 <<")
firstMethod()
