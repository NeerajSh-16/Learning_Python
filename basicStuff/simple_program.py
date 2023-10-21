#Celsius ---> Farenheit
#Via this simple program I got to know the working of the input and print functions along with
#manual typecasting and printing numbers with strings using only one print function
print("1st let's conert from Celsius to Farenheit")
cel =  float(input("Enter the temperature in Celsius : "))
far = 9/5*cel + 32
print("Temperature in Fahrenheit is : ",far)

print("Now we'll see Farhenheit to Celsius")
far = float(input("Enter the temperature in Farhenheit : "))
cel = (far - 32)*5/9
print("Temperature is Farhenheit is : ",cel)
