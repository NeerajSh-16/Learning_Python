# To make a list of 1st 10 Natural numbers
x = []
for i in range(10):
    z = (i+1) ** 2
    x.append(z)
print(x)

# We can do the same using the LIST COMPREHENSION

# Syntax : [ expression for item in list ]
x = [(i+1) ** 2 for i in range(10)]
print(x)

# print the squares of only 1st 5 even natural numbers
# Syntax : [ expression for item in list {if (test expression)}]
x = [(i+1)**2 for i in range(10) if (i%2 == 0)]
print(x)