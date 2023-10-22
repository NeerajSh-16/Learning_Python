# Lists in python are like Arrays in C++ but here they dont have the bounadtion  of holding same data type value

list1 = ['Neeraj','Sharma','is']
list2 = ['Madhav','Sharma']
print(list1+list2)

# Lists are MUTABLE
list3 = ['Disco',19.01,2001]
list3[0] += ' Deewane'
print(list3)
print(list3*3) # It's a new thing watch carefully

# To check if an element is present inside our list or not
list4 = ['Cricket','Football','Hockey','Badminton','Kabaddi']
print('Cricket' in list4)
print('Swimming' in list4)

# Adding new values and removing any value from our list
# Major difference between append and extend is that in later one we cam multiple elements while 1st one we can not
# MAjor differnece between remove and del is that with del we can remove multiple values
# Append and extend are used to add values at the end of our list
list5 = [10,20,30,40,50]
list5.append(60)
print(list5)
list5.extend([70,80])
print(list5)
list5.remove(80)
print(list5)
del(list5[6])
print(list5)
del(list5[2:5])
print(list5)

# Pushing (For pushing we've to use insert(index number,value to store at that index) and Poping inside list
list6 = ['Ritu','Neeraj','26-10-2001','19-01-2001']
print(list6)
list6.insert(4,'I love you Ritu')
print(list6)
list6.insert(5,'We will fight the matrix together')
print(list6)
list6.pop(5)
print(list6)

# To clear a list
list5.clear()
print(list5)

# Some more useful functions
list7 = [30,60,10,20,89,50,100,90,70]
# To sort our list
list7.sort()
print(list7)
# To reverse our list
list7.reverse()
print(list7)
# To find the index of a particular element in our list
print(list7.index(100))
# To find the length of our list
print(len(list7))

# List Slicing
# listX[N (Starting index), K+1 (ending index + 1), Interval (Not Necessary)]
list8 =   [10,20,30,40,50,60,70,80,90,100]
#Indexes   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list8[0:5])
# If we want to slice from starrt there's also another method
print(list8[:5])
####
print(list8[4:10])
# If we want to slice till end there's also another method
print(list8[4:])
# Using Interval while slicing
print(list8[0::2])
print(list8[0::3])
