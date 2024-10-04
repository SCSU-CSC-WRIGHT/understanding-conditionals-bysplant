# Temperature Check
temp_c = int(input("Enter the current temperature in Celsius "))
if (temp_c > 30):
    print("It's a hot day.")
else:
    print("The weather is cool.")

# Number Comparison
first_num = int(input("Enter one number "))
second_num = int(input("Enter second number "))
if (first_num > second_num) :
    print(first_num, "is greater than", second_num)
elif (first_num < second_num):
    print(second_num, "is greater than", first_num)
else: 
    print("They're equal.")

# Password Checker
admin_pw = "yaycats"
user_pw = input("Enter your password ")
if (admin_pw == user_pw):
    print("Access granted.")
if (admin_pw != user_pw):
    print("Access denied.")

# Simple Calculator
x = float(input("Enter one number "))
y = float(input("Enter second number "))
op = input("Enter an operation ")
if (op == "+"):
    print(x + y)
elif (op == "-"):
    print(x - y)
elif (op == "*"):
    print(x * y)
elif (op == "/"):
    print(x / y)
else:
    print("You didn't enter an operation")

# Positive, Negative, or Zero
num = int(input("Enter a number ")) 
if (num > 0):
    print("Your number is positive.")
elif (num == 0):
    print("Your number is zero.")
elif (num < 0):
    print("Your number is negative.")

# Day of the Week
num = int(input("Enter a number between 1 and 7 "))
if (num == 1):
    print("Monday")
elif (num == 2):
    print("Tuesday")
elif (num == 3):
    print("Wednesday")
elif (num == 4):
    print("Thursday")
elif (num == 5):
    print("Friday")
elif (num == 6):
    print("Saturday")
elif (num == 7):
    print("Sunday")
else:
    print("You didn't enter a number between 1 and 7.")"Sunday")
