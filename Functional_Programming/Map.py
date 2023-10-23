# Map is almost same as filter but with some minor difference
# Let's say that you want to find the square of a given number then we can do this in both ways
# either the traditional way or thw Python Map Way
# Let's explore the later one
# Syntax :
# map(function_name, iterable)
def find_sqr(a):
    return a ** 2

output = list(map(find_sqr,range(1,11)))
print(output)

# Now, what if we wanna do the same but with using the filter function
result = set(filter(lambda a : a ** 2,range(11)))
print(result)
