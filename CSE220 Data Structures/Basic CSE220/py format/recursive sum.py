# 1. Summation
def sum(i,n):
    if i <= n:
        return i + sum(i+1,n)
    else:
        return 0
print(sum(1,5))