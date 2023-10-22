# Writing by Method 1
file1 = open('temp.txt','w')
# Whenever you are using read, write or append functions always assign a variable to them because they return something
file_data_adder = file1.write('Hello Guys\nMy name is Neeraj Sharma\nAt present I\'m enrolled in M.C.A programme in NIT Jamshedpur')
# Also try this
# file_reader = file1.readlines()
print(file_data_adder)

file1.close()

# Reading by Method 2
with open('temp.txt','r') as file1:
    file_reader = file1.read()
    print(file_reader)

# Now we'll see data appending
file1 = open('temp.txt','a')
appending_file = file1.write("\nMy Roll Number is 2023PGCSCA022")
print(appending_file)

# Now, let's see thst how does this file looks
file1 = open('temp.txt','r')
file_reader = file1.read()
print(file_reader)