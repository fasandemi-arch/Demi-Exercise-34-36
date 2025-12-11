#Exercise 34: was about writing codes with while loop
# Start counting from 1
count = 1

# Loop while count is less than or equal to 5
while count <= 5:
    print("Number:", count)
    count += 1   # Increase count by 1 each loop
    # Start with an empty password

password = ""

# Continue asking until the correct password is entered
while password != "demi2008":
    password = input("Enter password: ")

# Loop ends when the password is correct
print("Access granted!")
#Exercise36:Designing and Debugging
x = 0

while x < 5:
    print(x)
# BUG: x never increases → infinite loop

x = 0

while x < 5:
    print(x)
    x += 1  # FIX: update variable to stop loop

    # Simple calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    # Debugging: check for division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operation")

    #Exercise35:Branches and Functions
    # Check if a number is positive, negative, or zero

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive")

elif num < 0:
    print("The number is negative")

else:
    print("The number is zero")

# Determine grade from score

score = int(input("Enter your score: "))

if score >= 70:
    print("Grade: A")

elif score >= 60:
    print("Grade: B")

elif score >= 50:
    print("Grade: C")

elif score >= 45:
    print("Grade: D")

else:
    print("Grade: F")







