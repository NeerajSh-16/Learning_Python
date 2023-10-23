# In Python we can add a function name to a variable
def add(i,j):
    return i+j

print(add(5,10))

a_variable = add
print(a_variable(20,30))

# In python we can return a function within another function
def call(i,j):
    return add(i,j)

print(call(40,60))

# In python we can also pass a function to function
def pas(i,j,passing_funtion):
    return passing_funtion(i,j)

print(pas(100,200,call))