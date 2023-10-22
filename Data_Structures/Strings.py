a = "neeraj sharma"
print(a.capitalize())
print(a.upper())

# To check if the input is an alphabet or a number

b = "2619"
print(b.isnumeric())

c = "Madhav is a bad boy, a very bad boy"
print(c.startswith('Madhav'))
print(c.endswith('girl'))
print(c.replace("Madhav","Neeraj"))

# To find the index of an element
print(c.find('a'))

d = '       Hello World'
print(d)
print(d.lstrip()) # Removes the space from the left side

# to convert a given string into a list
e = c.split()
print(e)
# to convert the whole string into a single element of a list
e = c.splitlines()
print(e)