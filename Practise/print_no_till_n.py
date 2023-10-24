'''
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:

Note that "" represents the consecutive values in between.
'''

if __name__ == '__main__':
    n = int(input("Enter the number : "))
    n_cpy = str(n)
    no_of_digits = len(n_cpy)
    temp = 0
    for i in range(n):
        itr_no = str(i+1)
        no_of_digits = len(itr_no)
        temp = temp * (10 ** no_of_digits) + (i+1)
    print(temp)