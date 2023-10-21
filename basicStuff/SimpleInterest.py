prin = float(input("Enter the principle amount : "))
rate = float(input("Enter the interest rate : "))
time = float(input("Enter the time period : "))
si = (prin*rate*time)/100
print("Your Simple interest on ",prin," for ",time," years at the rate of ",rate," % is ", si," Rs")