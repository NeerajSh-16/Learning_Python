# Let say that you want to print the name of a person with his today's lucky number
name = 'Neeraj'
luckyNumber = len(name)*3
print('Hello {}, your lucky number is {}'.format(name,luckyNumber))

example = 'format() method'
string = "This is an example of {} on a string ".format(example)
print(string)

first = "apple"
second = "ball"
third = "cat"
fourth = "dog"
fiffth = "elephant"
string2 = "a for {}, b for {}, c for {}, d for {} and e for {}".format(first,second,third,fourth,fiffth)
print(string2)

# Say you are getting a receipt of your purchase from a supermarket
price = 150000
with_tax = 10000
print("Your Purchase :\n One Plasma L.E.D Television : \t Rs {:.2f}\n With Tax : \t\t\t\t\t Rs {:.2f}".format(price,with_tax+price))
# Above in Rs {:.2f} it means that I want two digits after decimal point