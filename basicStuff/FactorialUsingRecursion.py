# Factorial of a number using recursion
def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))

num = int(input("Enter the number to find it's factorial : "))
fact = factorial(num)
print("Factorial of ", num ," is ",fact)