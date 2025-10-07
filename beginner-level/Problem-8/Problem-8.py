def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
A=5
print(factorial(A))