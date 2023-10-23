# Learning to use filter ( an in-built function )
# Syntax :
# filter (function, iterable)
# filter returns boolean value for each iterable

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# We've to find even numbers present inside that list
def find_even(a):
    return a%2 == 0

answer = set(filter(find_even,list1))
# Only those numbers wiil be printed which will return 'true'
print(answer)
# doing the same but by using lambda but for odd numbers and using 'range' function
answer = list(filter(lambda a : a & 1,range(41)))
print(answer)