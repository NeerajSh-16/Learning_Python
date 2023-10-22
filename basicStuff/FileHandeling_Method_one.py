file1 = open('temp.txt','w')

file_data_adder = file1.write('Hello Guys\nMy name is Neeraj Sharma\nAt present I\'m enrolled in M.C.A programme in NIT Jamshedpur')
# Also try this
# file_reader = file1.readlines()
print(file_data_adder)

file1.close()

# Method 2
with open('temp.txt','r') as file1:
    file_reader = file1.read()
    print(file_reader)