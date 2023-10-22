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

# To clear a list
list5.clear()
print(list5)
