# Here we'll learn about the lambda or anonymous functions
# Say we've a function which finds the square a number
def find_square(num):
    return num ** 2

print(find_square(5))

# Now, let's see this works with lambda
# Syntax of Lambda function :
# lambda ( a keyowrd ) argument ( which was paased to the original function) : expresion (which was written inside the function
fun = lambda num : num ** 2
output = fun(6)
print(output)

# lets see the case when we'll have to pass two arguments
fun = lambda a,b : a+b
output2 = fun(10,20)
print(output2)