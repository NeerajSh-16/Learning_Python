# Reduce
# It is a function in the 'functool' module in python which takes two arguments, 1si is function, 2nd is iterable
# Whenever we use 'reduce' function, instead of giving us another iterable as in filter and map it retruns a single value
import functools
def add(x,y):
    return x+y

output = functools.reduce(add,range(1,11))
print("Sum of first 10 Natural Numbers is : ",output)