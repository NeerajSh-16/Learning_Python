def add(a,b):
    return a+b

def square(a):
    return a ** 2

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
output = add(a,b)
print("Sum is : ",output)

# We can also pass function as arguments in python

output = square(add(a,b))
print("Square of the sum of ",a," and ",b," is ",output)

