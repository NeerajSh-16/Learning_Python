# Method 1
'''
file1 = open('temp.txt','r')
file1.close()
'''
# You must always close the file that you open by this method
# open() requires two arguments 1st one is location of the file that tyou want to open
# 2nd argument is the mode in which you want to open your file there are various modes like r(read), w(write),a(append),r+(read and write)

# Method 2
#with open ('temp.txt','r') as file1:
    #statement