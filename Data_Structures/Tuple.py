# Tuples
# NOTE
# Tuple -------> Immutable
# List  -------> Mutable

first_tuple = (1,2,3,4,5,6,7,8,9)
print(first_tuple)

# Concatination of two tuples
tuple1 = ('Neeraj',23)
tuple2 = ('Ritu',24)
tuple3 = ('We both love each other',3000)
print(tuple1 + tuple2 + tuple3)

# Finding the length of the tupple

tuple5 = ('Ritu','Neeraj',19,26,'5th August 2019')
print(tuple5)
print(len(tuple5))
# to print the index of an element inside a tuple
print(tuple5.index('5th August 2019'))

# Now we'll see the immutability of tuples
list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
print(list)
list[4] = 6
print(list)
# tuple(4) = 6 -------> This line will give you error
print(tuple)