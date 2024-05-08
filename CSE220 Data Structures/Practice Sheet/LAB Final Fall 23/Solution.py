def print_pattern(n):
    funCall(n, spaces = 0)

def funCall(n, spaces):
    if n >= 40:
        return
    print(" " * spaces, end="")
    pattern(n)
    print()
    funCall(n + 7, spaces + len(str(n)) + 1)

def pattern(n):
    if n >= 40:
        print(n, end=" ")
        return
    print(n, end=" ")
    pattern(n + 7)
    print(n, end=" ")

print('Sample Output 1')
n = 18
print_pattern(n)

print('Sample Output 2')
n = 12
print_pattern(n)