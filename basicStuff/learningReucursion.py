#Recursion
import sys
print(sys.getrecursionlimit()) # It will show us the default limit of recursive function calls
sys.setrecursionlimit(3000)# It will allow us to manually change the default recursive call limit
n = 1
def declartion_of_my_love_for_her():
    global n
    n = n + 1
    print("Neeraj Loves Ritu ...",n)
    declartion_of_my_love_for_her()

declartion_of_my_love_for_her()