def print_pattern(n):
    if n >= 47:
        return
    print(n, end=" ")
    print_pattern(n + 7)
    if n < 40:
        print(n, end=" ")

def call(n):
    if n < 40:
        print_pattern(n)
        print()
        call(n+7)
n = int(input())
call(n)