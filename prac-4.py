#factorial number:
print("Welcome to fctorial calculator!")
# taking input from user 
num = int(input("Please Enter your number: "))

factorial = 1

# checking if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(f"The factorial of {num} is, {factorial}")
