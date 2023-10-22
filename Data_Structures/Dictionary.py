# List ---> [] , index value
# List = [1,2,3,4,5...........]

# Dictionary ---> {} , key
# Dictionary = {key:value, key:value}

my_dict = {'key1':1, 'key2': '2', 'key3':[3,3,3],'key4':(444)}
print(my_dict)
for i in my_dict:
    print(my_dict[i])

dict = {1:'2',2:'3',3:'4',4:'5'}
print(my_dict)
for i in dict:
    print(dict[i])

# Some basic dictionary functions
dict = {'a':'apple','b':'ball','c':'cat','d':'dog'}

# add new element in a dictionary
dict['e'] = 'elephant'
print(dict)

# deleting an element from a dictionary
del(dict['b'])
print(dict)

# to check if a particular key is present inside a dictionary
print('e' in dict)
print('b' in dict)
print(dict.get('g'))
print(dict.get('g',"'g' not found"))

# to get all the keys and values respectively in a dictionary as a list
print(dict.keys())
print(dict.values())

